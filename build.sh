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

echo "==> Building Lecture 1 (Slidev)"
cd lecture-1-diffusion-policy
npm install
npx slidev build --base /lecture-1/
cd ..

echo "==> Copying lecture 1 build"
cp -r lecture-1-diffusion-policy/dist dist/lecture-1

echo "==> Done! Output in dist/"
ls -la dist/
