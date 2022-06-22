import pymongo

client = pymongo.MongoClient()
print(client)

db = client['starwars']
print(db)

# luke = db.characters.find_one({"name": "Luke Skywalker"})
# print(luke)
# print(luke['height'])
#
# # droids = db.characters.find(
# #     {"species.name": "Droid"}
# # )
# # for droid in droids:
# #     print(droid['name'])
#
# darth_vader = db.characters.find_one({"name": "Darth Vader"})
# print(darth_vader['name'], ",",  darth_vader['height'])
#
# yellow_eyes = db.characters.find({"eye_color": "yellow"})
# print(list(yellow['name'] for yellow in yellow_eyes))
#
# male_char = db.characters.find({"gender": "male"}).limit(3)
# print(list(male['name'] for male in male_char))
#
# alderaan_human = db.characters.find({"species.name": "Human", "homeworld.name": "Alderaan"})
# print(list(ald['name'] for ald in alderaan_human))


