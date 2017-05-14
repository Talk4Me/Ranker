import requests

FIREBASE_URL = "https://chatdb-80b85.firebaseio.com/Messages.json"

messages = requests.get(FIREBASE_URL).json()

rpc = {}
for message in messages:
	payload = ""
	for s in message["Messages"]:
		if s["Sent"]:
			payload += s["MessageBody"]
	rpc["message"] = message
	rpc["payload"] = payload

print rpc