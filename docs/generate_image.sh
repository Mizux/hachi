#!/usr/bin/env bash
set -eux

CDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$CDIR"

if [ -f "$CDIR/../venv/bin/activate" ]; then
  source "$CDIR/../venv/bin/activate"
elif [ -f "$CDIR/venv/bin/activate" ]; then
  source "$CDIR/venv/bin/activate"
fi

# Check plantuml is in PATH
command -v plantuml

# Run python scripts to regenerate dot and md files
python3 hachi.py
python3 pokemon.py

# Regenerate all svg files from dot files
rm -f *.svg
for i in *.dot; do
  plantuml --format svg "$i"
done
