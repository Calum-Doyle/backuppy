#!/bin/bash

set -e

APP_NAME="backuppy"
INSTALL_DIR="/usr/local/share/$APP_NAME"
BIN_DIR="/usr/local/bin"
LOG_DIR="/var/log/$APP_NAME"

if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root. Try: sudo $0"
    exit 1
fi

echo "Uninstalling $APP_NAME..."

rm -rf "$INSTALL_DIR" "$LOG_DIR"

echo "Done."
