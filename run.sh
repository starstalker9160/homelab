#!/bin/bash


# Delete cache from previous runs
cache_dirs=$(find . -type d -name "__pycache__")

if [ -n "$cache_dirs" ]; then
    find . -type d -name "__pycache__" -exec rm -rf {} +
    echo "[  OK  ] Cache cleared"
else
    echo "[  OK  ] No cache to clear"
fi

# Run marionette
python3 ~/Documents/homelab/marionette/main.py
