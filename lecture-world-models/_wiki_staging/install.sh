#!/bin/bash
# Copies staged wiki files into the Rajat Wiki vault.
# Run from any directory: bash _wiki_staging/install.sh

WIKI="/Users/raj/Desktop/Rajat Wiki"
STAGING="$(cd "$(dirname "$0")" && pwd)"

echo "Installing wiki updates from: $STAGING"
echo "Target wiki: $WIKI"
echo ""

# New pages
cp "$STAGING/wiki/V-JEPA 2.md" "$WIKI/wiki/V-JEPA 2.md"
echo "  [NEW]     wiki/V-JEPA 2.md"

cp "$STAGING/wiki/JEPA.md" "$WIKI/wiki/JEPA.md"
echo "  [NEW]     wiki/JEPA.md"

# Updated pages
cp "$STAGING/wiki/Raj - Preferences and Decisions.md" "$WIKI/wiki/Raj - Preferences and Decisions.md"
echo "  [UPDATE]  wiki/Raj - Preferences and Decisions.md"

cp "$STAGING/index/Map of Content.md" "$WIKI/index/Map of Content.md"
echo "  [UPDATE]  index/Map of Content.md"

# Source log
cp "$STAGING/sources/2026-04-15-vjepa2-lecture-slides.md" "$WIKI/sources/2026-04-15-vjepa2-lecture-slides.md"
echo "  [NEW]     sources/2026-04-15-vjepa2-lecture-slides.md"

echo ""
echo "Done! 5 files installed. You can now delete _wiki_staging/:"
echo "  rm -rf \"$STAGING\""
