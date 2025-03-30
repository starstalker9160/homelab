#!/bin/bash

set -e
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"


is_installed() {
    command -v "$1" &>/dev/null
}


MISSING_PACKAGES=()
if ! is_installed python3; then
    MISSING_PACKAGES+=(python3)
fi
if ! is_installed jq; then
    MISSING_PACKAGES+=(jq)
fi

if [ ${#MISSING_PACKAGES[@]} -eq 0 ]; then
    log 0 "All required packages are already installed."
    exit 0
fi


if command -v apt-get &>/dev/null; then
    PKG_MANAGER="apt-get"
    UPDATE_CMD="sudo apt-get update"
    INSTALL_CMD="sudo apt-get install -y"
elif command -v dnf &>/dev/null; then
    PKG_MANAGER="dnf"
    UPDATE_CMD="sudo dnf check-update"
    INSTALL_CMD="sudo dnf install -y"
elif command -v yum &>/dev/null; then
    PKG_MANAGER="yum"
    UPDATE_CMD="sudo yum check-update"
    INSTALL_CMD="sudo yum install -y"
elif command -v pacman &>/dev/null; then
    PKG_MANAGER="pacman"
    UPDATE_CMD="sudo pacman -Sy"
    INSTALL_CMD="sudo pacman -S --noconfirm"
elif command -v zypper &>/dev/null; then
    PKG_MANAGER="zypper"
    UPDATE_CMD="sudo zypper refresh"
    INSTALL_CMD="sudo zypper install -y"
else
    log 3 "Unsupported package manager. Please install required packages manually."
    exit 1
fi


log 0 "Updating package lists..."
$UPDATE_CMD || catch "Failed to update package lists."

log 0 "Installing missing packages: ${MISSING_PACKAGES[*]}"
$INSTALL_CMD "${MISSING_PACKAGES[@]}" || catch "Failed to install required packages."


log 0 "Installation complete. Run run.sh"