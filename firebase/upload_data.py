# File: firebase/upload_data.py
import requests
import sys
import json

FIREBASE_URL = "https://guacamole-a69bd-default-rtdb.asia-southeast1.firebasedatabase.app"

if len(sys.argv) != 3:
    print("Usage: python upload_data.py <key> <value>")
    sys.exit(1)

key = sys.argv[1]
value = sys.argv[2]

res = requests.put(f"{FIREBASE_URL.rstrip('/')}/{key}.json", data=json.dumps(value))
print("Upload result:", res.status_code, res.text)

