# Variables
CWD="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REQUIRED_PACKAGES=(python3 jq)


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

is_installed() {
    command -v "$1" &>/dev/null
}