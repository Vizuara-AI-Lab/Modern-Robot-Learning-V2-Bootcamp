#!/bin/bash
set -e

echo "==> Cleaning dist/"
rm -rf dist
mkdir -p dist

echo "==> Copying homepage"
cp -r site/* dist/

echo "==> Copying shared assets for homepage"
cp lecture-1-diffusion-policy/public/vizuara-logo.png dist/
cp site/lecture-1-thumb.png dist/
cp lecture-2-vla/public/figures/pi0-full-architecture.png dist/lecture-2-thumb.png
cp site/lecture-3-thumb.png dist/

echo "==> Building Lecture 1 (Slidev)"
cd lecture-1-diffusion-policy
npm install
npx slidev build --base /lecture-1/
cd ..

echo "==> Copying lecture 1 build"
cp -r lecture-1-diffusion-policy/dist dist/lecture-1

echo "==> Building Lecture 2 (Slidev)"
cd lecture-2-vla
npm install
npx slidev build --base /lecture-2/
cd ..

echo "==> Copying lecture 2 build"
cp -r lecture-2-vla/dist dist/lecture-2

echo "==> Building Lecture 3 (Slidev)"
cd lecture-3-deploy
npm install
npx slidev build --base /lecture-3/
cd ..

echo "==> Copying lecture 3 build"
cp -r lecture-3-deploy/dist dist/lecture-3

echo "==> Copying lecture 4 thumbnail"
cp site/lecture-4-thumb.png dist/

echo "==> Building Lecture 4 Part 1 (Slidev)"
cd lecture-world-models
npm install
if npx slidev build --base /lecture-4/; then
  cd ..
  echo "==> Copying lecture 4 part 1 build"
  cp -r lecture-world-models/dist dist/lecture-4
else
  cd ..
  echo "==> WARN: Lecture 4 Part 1 build failed, skipping"
fi

echo "==> Building Lecture 4 Part 2 (Slidev)"
cd lecture-world-models-part2
npm install
if npx slidev build --base /lecture-4-part2/; then
  cd ..
  echo "==> Copying lecture 4 part 2 build"
  cp -r lecture-world-models-part2/dist dist/lecture-4-part2
else
  cd ..
  echo "==> WARN: Lecture 4 Part 2 build failed, skipping"
fi

echo "==> Copying lecture 5 thumbnail"
cp site/lecture-5-thumb.png dist/

echo "==> Building Lecture 5: JEPA (Slidev)"
cd lecture-world-models-jepa
npm install
if npx slidev build --base /lecture-5/; then
  cd ..
  echo "==> Copying lecture 5 build"
  cp -r lecture-world-models-jepa/dist dist/lecture-5
else
  cd ..
  echo "==> WARN: Lecture 5 build failed, skipping"
fi

echo "==> Copying lecture 6 thumbnail"
cp site/lecture-6-thumb.png dist/

echo "==> Building Lecture 6: Two Paradigms of World Models (Slidev)"
cd lecture-world-models-paradigms
npm install
if npx slidev build --base /lecture-6/; then
  cd ..
  echo "==> Copying lecture 6 build"
  cp -r lecture-world-models-paradigms/dist dist/lecture-6
else
  cd ..
  echo "==> WARN: Lecture 6 build failed, skipping"
fi

echo "==> Done! Output in dist/"
ls -la dist/
