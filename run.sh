#!/bin/bash

# Variables
CWD="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CACHE_DIRS=$(find . -type d -name "__pycache__")


# Delete cache from previous runs
if [ -n "$CACHE_DIRS" ]; then
    find . -type d -name "__pycache__" -exec rm -rf {} +
    echo "[  OK  ] Cache cleared"
else
    echo "[  OK  ] No cache to clear"
fi

# Run marionette
python "$CWD/marionette/main.py"
