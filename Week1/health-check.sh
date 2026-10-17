#!/usr/bin/env bash
set -u

CONFIG_FILE="${1:-app.conf}"

if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "FAIL: Missing configuration: $CONFIG_FILE" >&2
    exit 1
fi

if [[ ! -r "$CONFIG_FILE" ]]; then
    echo "FAIL: Configuration is not readable" >&2
    exit 2
fi

APP_ENV=$(grep '^APP_ENV=' "$CONFIG_FILE" | head -n 1 | cut -d '=' -f 2-)

if [[ -z "$APP_ENV" ]]; then
    echo "FAIL: APP_ENV is missing or empty" >&2
    exit 3
fi

case "$APP_ENV" in
    development|testing|production)
        echo "PASS: Configuration valid for $APP_ENV"
        exit 0
        ;;
    *)
        echo "FAIL: Unsupported APP_ENV value: $APP_ENV" >&2
        exit 4
        ;;
esac
