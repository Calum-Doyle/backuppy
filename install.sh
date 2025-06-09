#!/bin/bash

set -e

APP_NAME="backuppy"
STATE_SRC="data.json"
APP_SRC="backuppy"

INSTALL_DIR="/usr/local/share/$APP_NAME"
BIN_PATH="/usr/local/bin"
LOG_DIR="/var/log/$APP_NAME"

if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root. Try: sudo $0"
    exit 1
fi

echo "Installing $APP_NAME..."

mkdir -p "$INSTALL_DIR"

cp "$APP_SRC" "$INSTALL_DIR/"
cp "$STATE_SRC" "$INSTALL_DIR/"

chmod +x "$INSTALL_DIR/$APP_NAME"

ln -sf "$INSTALL_DIR/$APP_NAME" "$BIN_PATH/$APP_NAME"

mkdir -p "$LOG_DIR"
chmod 755 "$LOG_DIR"

echo "Done."
