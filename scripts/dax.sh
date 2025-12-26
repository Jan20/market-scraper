#!/bin/sh

set -eu

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ -z "$DAX_URL" ]; then
  echo "Error: $DAX_URL is not defined."
  exit 1
fi

curl --location "$DAX_URL" -o "$SCRIPT_DIR/temp.html"

curl --location 'http://localhost:8080/market' \
--header 'Content-Type: application/json' \
--data '{
    "market": "dax"
}' -o "$DAX_FILE_PATH"
