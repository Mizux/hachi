#!/usr/bin/env bash
set -eux

CDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$CDIR"

if [ -f "$CDIR/../venv/bin/activate" ]; then
  source "$CDIR/../venv/bin/activate"
elif [ -f "$CDIR/venv/bin/activate" ]; then
  source "$CDIR/venv/bin/activate"
fi

# Run python scripts to regenerate md files (including mermaid graphs)
python3 hachi.py
python3 pokemon.py
