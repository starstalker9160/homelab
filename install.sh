#!/bin/bash

set -euo pipefail
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

log 0 "Starting installation script..."

MISSING_PACKAGES=()

for pkg in "${REQUIRED_PACKAGES[@]}"; do
    if ! is_installed "$pkg"; then
        MISSING_PACKAGES+=("$pkg")
    fi
done

if (( ${#MISSING_PACKAGES[@]} > 0 )); then
    log 3 "Missing packages, please install manually: ${MISSING_PACKAGES[*]}"
    exit 1
fi
log 0 "No missing packages"

log 0 "Generating requirements.txt"
python3 "$CWD/tools/auto_fill_requirements.py"
log 0 "Installing required python packages"
python3 -m pip install -r requirements.txt

log 0 "Installation complete! Run run.sh"