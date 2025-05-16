import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python fetch_data.py <firebase_url> <key>")
    sys.exit(1)

firebase_url = sys.argv[1].rstrip('/')
key = sys.argv[2]
res = requests.get(f"{firebase_url}/{key}.json")
print(res.text.strip('"'))
