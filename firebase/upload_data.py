import requests
import sys
import json

if len(sys.argv) != 4:
    print("Usage: python upload_data.py <firebase_url> <key> <value>")
    sys.exit(1)

firebase_url = sys.argv[1].rstrip('/')
key = sys.argv[2]
value = sys.argv[3]

res = requests.put(f"{firebase_url}/{key}.json", data=json.dumps(value))
print("Upload result:", res.status_code, res.text)
