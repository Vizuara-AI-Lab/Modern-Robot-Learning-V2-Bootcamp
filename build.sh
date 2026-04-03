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

echo "==> Done! Output in dist/"
ls -la dist/
