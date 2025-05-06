
import firebase_admin
from firebase_admin import credentials, db
import os

cred = credentials.Certificate('creds.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://loudwave-54180-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference(f"users/{os.environ['UID']}/url")
ref.set(os.environ['NGROK_URL'])

# Also print the URL in a loop like before
url = os.environ['NGROK_URL']
for i in range(5):
    print(f"noVNC Link: {url}")
