#!/bin/bash

set -e
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"


# Variables
M_VER=$(jq -r '.marionetteVersion // empty' desc.json)


# Actual stuff
if [ "$(id -u)" -ne 0 ]; then
    log 3 "Please run the script as sudo"
    exit 1
fi

if ! command -v jq &>/dev/null; then
    log 3 "Missing required libraries, run install.sh first"
    exit 1
fi

if [ ! -f desc.json ]; then
    log 3 "desc.json not found"
    exit 1
fi

if [ -z "$M_VER" ]; then
    log 3 "marionette version not found."
    exit 1
fi


if find . -type d -name "__pycache__" | grep -q .; then
    find . -type d -name "__pycache__" -exec rm -rf {} +
    log 0 "Cache cleared"
else
    log 0 "No cache to clear"
fi


echo "marionette version: $M_VER"

# Run marionette
sudo python "$CWD/marionette/main.py" || catch "Failed to run marionette (as sudo)"
