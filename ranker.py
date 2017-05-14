import requests
import json

FIREBASE_URL = "https://chatdb-80b85.firebaseio.com/Messages.json"
PERSAN_URL = 'http://127.0.0.1:5000/PersonaliTyzer'

convos = requests.get(FIREBASE_URL).json()
print(json.dumps(convos))
rpc = {}
for convo in convos:
	print 
	payload = ""
	for s in convo["Messages"]:
		if s["Sent"]:
			payload += s["MessageBody"]
	rpc["message"] = payload

	#vector = {"Openness":0.5, "Conscientiousness":0.5, "Extraversion":0.5, "Agreeableness":0.5, "Emotional range":0.5, 
	vector = {"Curiosity":1}
	matchDist = requests.post(PERSAN_URL, data=json.dumps({"text":payload, "vector":vector}))

	print convo['id']
	print matchDist.content
