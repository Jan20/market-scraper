#!/bin/sh

set -eu

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ -z "$NASDAQ_URL" ]; then
  echo "Error: $NASDAQ_URL is not defined."
  exit 1
fi

curl --location "$NASDAQ_URL" -o "$SCRIPT_DIR/temp.html"

curl --location 'http://localhost:8080/market' \
--header 'Content-Type: application/json' \
--data '{
    "market": "nasdaq"
}' -o "$NASDAQ_FILE_PATH"
