import requests

FIREBASE_URL = "https://chatdb-80b85.firebaseio.com/Messages.json"

messages = requests.get(FIREBASE_URL).json()

print messages