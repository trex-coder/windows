# File: firebase/fetch_data.py
import requests
import sys

FIREBASE_URL = "https://guacamole-a69bd-default-rtdb.asia-southeast1.firebasedatabase.app"

if len(sys.argv) != 2:
    print("Usage: python fetch_data.py <key>")
    sys.exit(1)

key = sys.argv[1]
res = requests.get(f"{FIREBASE_URL.rstrip('/')}/{key}.json")
print(res.text.strip('"'))
