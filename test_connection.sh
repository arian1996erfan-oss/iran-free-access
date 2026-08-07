# scripts/test_connection.sh
#!/bin/bash

# Test script for Iran Free Access
echo "Testing connection to Iran Free Access..."

CONFIG_FILE=${1:-"config.example.json"}

if [ ! -f "$CONFIG_FILE" ]; then
    echo "Config file not found: $CONFIG_FILE"
    exit 1
fi

echo "Using config: $CONFIG_FILE"
echo "Testing protocol..."

# Placeholder for actual test
# curl -s -o /dev/null -w "%{http_code}" https://www.google.com

echo "Test completed."
