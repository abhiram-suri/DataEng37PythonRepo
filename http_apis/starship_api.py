import requests
import pymongo

client = pymongo.MongoClient()
db = client['starwars']

sw_req = requests.get("https://swapi.dev/api/starships/10")
sws = sw_req.json()['pilots']

pilot_name = []
for s in sws:
    pil_req = requests.get(s)
    pil = pil_req.json()['name']
    pilot_name.append(pil)

p_id = []
for p in pilot_name:
    pilot_id = db.characters.find_one({"name": p}, {"_id": 1})
    p_id.append(pilot_id)

print(p_id)