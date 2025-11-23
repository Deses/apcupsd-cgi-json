#!/usr/bin/env python3
import subprocess
import json
import sys

def get_apcaccess(host='127.0.0.1:3551'):
    try:
        p = subprocess.run(['/usr/sbin/apcaccess', 'status', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        out = p.stdout
    except Exception as e:
        out = ''
    return out

def parse_output(text):
    data = {}
    for line in text.splitlines():
        if not line.strip():
            continue
        if ':' in line:
            key, val = line.split(':', 1)
            data[key.strip()] = val.strip()
    return data

def main():
    text = get_apcaccess('127.0.0.1:3551')
    if not text:
        print('Status: 500 Internal Server Error')
        print('Content-Type: application/json')
        print()
        print(json.dumps({'error': 'no data'}))
        sys.exit(1)
    data = parse_output(text)
    print('Content-Type: application/json')
    print()
    print(json.dumps(data))

if __name__ == "__main__":
    main()
