#!/bin/bash

# Variables
CWD="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CACHE_DIRS=$(find . -type d -name "__pycache__")


# Functions
log() {
    local c=(32 34 33 31) t=("  OK  " " INFO " " WARN " " FAIL ")
    local tag="\e[37m[\e[${c[$1]:-37}m${t[$1]:-????}\e[37m]\e[0m"
    echo -e "$tag $2\e[0m"
}

catch() {
    log 3 "An error occurred: $1"
    exit 1
}


# Delete cache from previous runs

if [ "$(id -u)" -ne 0 ]; then
    log 3 "Please run the script as sudo"
fi

if [ -n "$CACHE_DIRS" ]; then
    find . -type d -name "__pycache__" -exec rm -rf {} +
    log 0 "Cache cleared"
else
    log 0 "No cache to clear"
fi


# Run marionette
python "$CWD/marionette/main.py" || catch "Failed to run marionette"
