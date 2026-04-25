<template>
  <div>
    <!-- Toolbar -->
    <div class="toolbar-buttons">
      <button @click="addSlide" class="tool-btn add-btn" title="Add blank slide after current">+</button>
      <button @click="copyDrawing" class="tool-btn copy-btn" title="Copy this slide's drawings">✂</button>
      <button v-if="copiedSlide > 0" @click="pasteDrawing" class="tool-btn paste-btn" title="Paste drawings into this slide">📋</button>
      <div v-if="toast" class="toast-msg">{{ toast }}</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { drawingState } from '@slidev/client/state/drawings.ts'

const copiedSlide = ref(0)
const toast = ref('')
let toastTimer = null
let pasteHandler = null

function getPage() {
  return parseInt(window.location.pathname.replace(/\//g, '')) || 1
}

function showToast(msg, ms = 3000) {
  toast.value = msg
  clearTimeout(toastTimer)
  toastTimer = setTimeout(() => { toast.value = '' }, ms)
}

// Shift drawings by POSTing directly to Vite's server-reactive endpoint.
// This updates the server's in-memory state and persists SVGs to disk.
async function shiftDrawingsOnServer(afterSlide) {
  const patch = {}
  const keys = Object.keys(drawingState).map(Number).filter(n => n > afterSlide).sort((a, b) => b - a)
  for (const n of keys) {
    patch[n + 1] = drawingState[n]
  }
  // Clear the slot for the new blank slide
  if (drawingState[afterSlide + 1] !== undefined) {
    patch[afterSlide + 1] = null
  }
  if (Object.keys(patch).length === 0) return
  await fetch('/@server-reactive/drawings', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ source: 'add-slide', patch, timestamp: Date.now() })
  })
}

async function addSlide() {
  const page = getPage()
  try {
    const res = await fetch(`http://localhost:3099/add-slide?after=${page}`)
    const data = await res.json()
    if (data.ok) {
      // Shift drawings on the Vite server directly, then navigate
      await shiftDrawingsOnServer(page)
      showToast('Slide added!')
      setTimeout(() => {
        window.location.assign(window.location.origin + '/' + data.newSlide)
      }, 400)
    }
  } catch (e) { showToast('Add slide failed: ' + e.message) }
}

function copyDrawing() {
  const page = getPage()
  copiedSlide.value = page
  showToast(`Slide ${page} drawings copied! Go to target slide and click 📋 or Ctrl+V`, 4000)
}

async function pasteDrawing() {
  if (copiedSlide.value <= 0) return
  const page = getPage()
  if (page === copiedSlide.value) {
    showToast('Navigate to a different slide first')
    return
  }
  try {
    const res = await fetch(`http://localhost:3099/copy-drawing?from=${copiedSlide.value}&to=${page}`)
    const data = await res.json()
    if (data.ok) {
      showToast(`Drawings from slide ${copiedSlide.value} pasted to slide ${page}!`)
      setTimeout(() => { window.location.reload() }, 800)
    } else {
      showToast('Paste failed: ' + (data.error || 'unknown'))
    }
  } catch (e) {
    showToast('Paste failed — is the server running?')
  }
}

onMounted(() => {
  pasteHandler = (e) => {
    if (copiedSlide.value <= 0) return
    e.preventDefault()
    pasteDrawing()
  }
  document.addEventListener('paste', pasteHandler)
})

onBeforeUnmount(() => {
  if (pasteHandler) document.removeEventListener('paste', pasteHandler)
})
</script>

<style>
.toolbar-buttons {
  position: fixed;
  bottom: 70px; right: 24px;
  display: flex; flex-direction: column; gap: 8px;
  z-index: 200; align-items: center;
}
.tool-btn {
  width: 36px; height: 36px; border-radius: 50%;
  background: #c2785c; color: #fff;
  font-size: 18px; font-weight: 700;
  border: none; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
  opacity: 0.5; transition: opacity 0.2s, background 0.2s;
  font-family: -apple-system, sans-serif;
  line-height: 1; padding: 0;
}
.tool-btn:hover { opacity: 1; }
.add-btn { font-size: 22px; }
.paste-btn { background: #5a7fa5; opacity: 0.7; }
.paste-btn:hover { opacity: 1; }

.toast-msg {
  position: fixed; bottom: 130px; right: 24px;
  background: rgba(58,48,37,0.9); color: #fff;
  padding: 8px 16px; border-radius: 8px;
  font-size: 13px; font-family: -apple-system, sans-serif;
  white-space: nowrap; pointer-events: none;
  animation: toast-in 0.2s ease-out;
}
@keyframes toast-in {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
