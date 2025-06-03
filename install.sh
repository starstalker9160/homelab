#!/bin/bash

set -euo pipefail
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

log 0 "Starting installation script..."

MISSING_PACKAGES=()
if ! is_installed python3; then
    MISSING_PACKAGES+=(python3)
fi

log 3 "Missing packages: ${MISSING_PACKAGES[*]}"