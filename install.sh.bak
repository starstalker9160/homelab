#!/bin/bash

set -euo pipefail  # Exit on error, unset variables, and pipe failures
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

log 0 "Starting installation script..."

is_installed() {
    command -v "$1" &>/dev/null
}

MISSING_PACKAGES=()
if ! is_installed python3; then
    MISSING_PACKAGES+=(python3)
fi
if ! is_installed python-psutil; then
    MISSING_PACKAGES+=(python-psutil)
fi
if ! is_installed jq; then
    MISSING_PACKAGES+=(jq)
fi

if [ ${#MISSING_PACKAGES[@]} -eq 0 ]; then
    log 0 "All required packages are already installed."
    exit 0
fi

log 0 "Installing missing packages: ${MISSING_PACKAGES[*]}"


# Detect Package Manager
declare -A PACKAGE_MANAGERS=(
    ["apt-get"]="sudo apt-get update && sudo apt-get install -y"
    ["dnf"]="sudo dnf check-update && sudo dnf install -y"
    ["yum"]="sudo yum check-update && sudo yum install -y"
    ["pacman"]="sudo pacman -Sy && sudo pacman -S --noconfirm"
    ["zypper"]="sudo zypper refresh && sudo zypper install -y"
)

for pkg_manager in "${!PACKAGE_MANAGERS[@]}"; do
    if command -v "$pkg_manager" &>/dev/null; then
        PKG_MANAGER="$pkg_manager"
        INSTALL_CMD="${PACKAGE_MANAGERS[$pkg_manager]}"
        break
    fi
done

if [ -z "${PKG_MANAGER:-}" ]; then
    log 3 "Unsupported package manager. Please install required packages manually."
    exit 1
fi

log 0 "Updating package lists..."
if ! eval "$INSTALL_CMD ${MISSING_PACKAGES[*]}"; then
    catch "Failed to update and install packages."
    exit 1
fi


log 0 "Installation complete. Run run.sh"
