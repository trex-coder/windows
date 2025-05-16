import requests
import sys
import json

if len(sys.argv) != 3:
    print("Usage: python upload_rdp_address.py <firebase_url> <rdp_address>")
    sys.exit(1)

firebase_url = sys.argv[1].rstrip('/')
rdp_address = sys.argv[2]

res = requests.put(f"{firebase_url}/rdpAddress.json", data=json.dumps(rdp_address))
print("Upload result:", res.status_code, res.text)
