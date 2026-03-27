const http = require('http');
const fs = require('fs');
const path = require('path');

const SLIDES_PATH = path.join(__dirname, 'slides.md');
const PORT = 3099;

// Parse slides.md into an array of { startLine, endLine } for each slide
function parseSlides() {
  const content = fs.readFileSync(SLIDES_PATH, 'utf-8');
  const lines = content.split('\n');
  const slides = [];
  let i = 0;

  // Skip global frontmatter: opening --- then closing ---
  while (i < lines.length && lines[i].trim() !== '---') i++;
  i++;
  while (i < lines.length && lines[i].trim() !== '---') i++;
  i++;

  let slideStart = i;

  while (i < lines.length) {
    if (lines[i].trim() === '---') {
      // End current slide
      slides.push({ startLine: slideStart, endLine: i });

      // Check if next block is per-slide frontmatter
      let j = i + 1;
      let isYaml = true;
      while (j < lines.length && lines[j].trim() !== '---') {
        const t = lines[j].trim();
        if (t && !t.match(/^[\w-]+\s*:/)) {
          isYaml = false;
          break;
        }
        j++;
      }
      if (isYaml && j < lines.length && j - i < 8 && lines[j].trim() === '---') {
        slideStart = i; // include the --- and frontmatter
        i = j + 1;
      } else {
        slideStart = i + 1;
        i++;
      }
    } else {
      i++;
    }
  }

  // Last slide
  if (slideStart < lines.length) {
    slides.push({ startLine: slideStart, endLine: lines.length });
  }

  return { lines, slides };
}

// Shift drawing SVG files so they stay aligned with their slides after insertion
function shiftDrawings(afterSlideNumber) {
  if (!fs.existsSync(DRAWINGS_DIR)) return;
  const files = fs.readdirSync(DRAWINGS_DIR);
  // Collect slide numbers that have SVG files and need shifting
  const nums = [];
  for (const f of files) {
    const m = f.match(/^(\d+)\.svg$/);
    if (m) {
      const n = parseInt(m[1]);
      if (n > afterSlideNumber) nums.push(n);
    }
  }
  // Rename from highest to lowest to avoid overwriting
  nums.sort((a, b) => b - a);
  for (const n of nums) {
    fs.renameSync(
      path.join(DRAWINGS_DIR, `${n}.svg`),
      path.join(DRAWINGS_DIR, `${n + 1}.svg`)
    );
  }
}

// Prepare the new file content but don't write yet (returns content string + result)
function prepareBlankSlide(afterSlideNumber) {
  const { lines, slides } = parseSlides();

  if (afterSlideNumber <= slides.length) {
    const insertAt = slides[afterSlideNumber - 1].endLine;
    const before = lines.slice(0, insertAt);
    const blank = ['', '---', '', '<div style="height:1px;"></div>', ''];
    const after = lines.slice(insertAt);
    return {
      content: [...before, ...blank, ...after].join('\n'),
      result: { ok: true, newSlide: afterSlideNumber + 1 }
    };
  }

  // Beyond end — append
  const content = fs.readFileSync(SLIDES_PATH, 'utf-8');
  return {
    content: content + '\n\n---\n\n<div style="height:1px;"></div>\n',
    result: { ok: true, newSlide: slides.length + 2 }
  };
}

function getSlideSource(slideNumber) {
  const { lines, slides } = parseSlides();
  if (slideNumber < 1 || slideNumber > slides.length) {
    return { ok: false, error: `Slide ${slideNumber} not found (total: ${slides.length})` };
  }
  const slide = slides[slideNumber - 1];
  const source = lines.slice(slide.startLine, slide.endLine).join('\n').trim();
  return { ok: true, source, slideNumber, totalSlides: slides.length };
}

function pasteSourceIntoSlide(slideNumber, source) {
  const { lines, slides } = parseSlides();
  if (slideNumber < 1 || slideNumber > slides.length) {
    return { ok: false, error: `Slide ${slideNumber} not found` };
  }
  const slide = slides[slideNumber - 1];

  // Replace the slide content (between its start and the next ---)
  const before = lines.slice(0, slide.startLine);
  const after = lines.slice(slide.endLine);
  const newContent = ['', source, ''];

  fs.writeFileSync(SLIDES_PATH, [...before, ...newContent, ...after].join('\n'));
  return { ok: true };
}

const DRAWINGS_DIR = path.join(__dirname, '.slidev', 'drawings', 'slides');

function copyDrawing(fromSlide, toSlide) {
  const srcFile = path.join(DRAWINGS_DIR, `${fromSlide}.svg`);
  const destFile = path.join(DRAWINGS_DIR, `${toSlide}.svg`);
  if (!fs.existsSync(srcFile)) {
    return { ok: false, error: `No drawing on slide ${fromSlide}` };
  }
  fs.copyFileSync(srcFile, destFile);
  return { ok: true };
}

const server = http.createServer((req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') { res.writeHead(204); return res.end(); }

  const url = new URL(req.url, `http://localhost:${PORT}`);

  if (url.pathname === '/add-slide' && req.method === 'GET') {
    const after = parseInt(url.searchParams.get('after') || '1');
    try {
      const { content, result } = prepareBlankSlide(after);
      // Send response first — client shifts drawings via direct POST to
      // Slidev's server-reactive endpoint, then navigates.
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify(result));
      // Delete the SVG for the new blank slot — the client's shift POST
      // sets it to null in memory but writeDrawings doesn't delete files.
      setTimeout(() => {
        const blankSvg = path.join(DRAWINGS_DIR, `${after + 1}.svg`);
        if (fs.existsSync(blankSvg)) fs.unlinkSync(blankSvg);
      }, 200);
      // Write markdown after delay so HMR doesn't kill the fetch callback.
      setTimeout(() => { fs.writeFileSync(SLIDES_PATH, content); }, 800);
    } catch (e) {
      res.writeHead(500, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: e.message }));
    }
  } else if (url.pathname === '/get-slide-source' && req.method === 'GET') {
    const slide = parseInt(url.searchParams.get('slide') || '1');
    try {
      const result = getSlideSource(slide);
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify(result));
    } catch (e) {
      res.writeHead(500, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: e.message }));
    }
  } else if (url.pathname === '/paste-content' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const { slide, source } = JSON.parse(body);
        if (!slide || !source) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          return res.end(JSON.stringify({ error: 'Missing slide or source' }));
        }
        const result = pasteSourceIntoSlide(slide, source);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(result));
      } catch (e) {
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: e.message }));
      }
    });
  } else if (url.pathname === '/copy-drawing' && req.method === 'GET') {
    const from = parseInt(url.searchParams.get('from') || '0');
    const to = parseInt(url.searchParams.get('to') || '0');
    try {
      const result = copyDrawing(from, to);
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify(result));
    } catch (e) {
      res.writeHead(500, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: e.message }));
    }
  } else {
    res.writeHead(404);
    res.end('Not found');
  }
});

server.listen(PORT, () => {
  console.log(`Add-slide server running on http://localhost:${PORT}`);
  console.log(`Endpoints: GET /add-slide?after=N, GET /get-slide-source?slide=N, POST /paste-content {slide, source}`);
});
