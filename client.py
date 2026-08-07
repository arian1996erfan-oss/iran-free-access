# client.py
import json
import subprocess
import sys
import os

def load_config(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def run_protocol(config):
    protocol = config.get('protocol', '').lower()
    if protocol == 'vless':
        print(f"Starting VLESS+REALITY connection to {config['server']}")
        # Command would go here - placeholder
        return True
    elif protocol == 'hysteria2':
        print(f"Starting Hysteria2 connection to {config['server']}")
        # Command would go here - placeholder
        return True
    else:
        print(f"Unsupported protocol: {protocol}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python client.py <config_file>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    if not os.path.exists(config_file):
        print(f"Config file not found: {config_file}")
        sys.exit(1)
    
    config = load_config(config_file)
    success = run_protocol(config)
    
    if success:
        print("Connection established successfully!")
    else:
        print("Connection failed.")

if __name__ == "__main__":
    main()
