#!/bin/bash

PHRASE=$1
PROXY_URL=$2

if [ -z "$PHRASE" ]; then
    echo "Usage: ./run_scraper.sh [phrase] [proxy_url]"
    exit 1
fi

if [ -z "$PROXY_URL" ]; then
    echo "Running: python3 wikipedia_scraper.py \"$PHRASE\""
    python wikipedia_scraper.py "$PHRASE"
else
    echo "Running: python3 wikipedia_scraper.py \"$PHRASE\" \"$PROXY_URL\""
    python wikipedia_scraper.py "$PHRASE" "$PROXY_URL"
fi
