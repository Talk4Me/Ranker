import requests
import json

FIREBASE_URL = "https://chatdb-80b85.firebaseio.com/Messages.json"
PERSAN_URL = 'http://127.0.0.1:5000/PersonaliTyzer'

messages = requests.get(FIREBASE_URL).json()

rpc = {}
for message in messages:
	payload = ""
	for s in message["Messages"]:
		if s["Sent"]:
			payload += s["MessageBody"]
	rpc["message"] = message
	rpc["payload"] = payload

vector = {"Openness":0.5, "Conscientiousness":0.5, "Extraversion":0.5, "Agreeableness":0.5, "Emotional range":0.5}
matchDist = requests.post(PERSAN_URL, data=json.dumps({"text":payload, "vector":vector}))

print rpc
print matchDist.content
