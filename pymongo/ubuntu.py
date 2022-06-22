import pymongo

client = pymongo.MongoClient("52.28.114.66")

db = client['test_database']

collection = db['customers']

mydict = {"name": "David", "company": "Sparta Global"}

x = collection.insert_one(mydict)
result = collection.find({})

for r in result:
    print(r)

