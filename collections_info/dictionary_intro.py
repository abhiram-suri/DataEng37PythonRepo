# # Dictionaries
#
# data_eng_37 = {
#     "course_name": "Data Engineering 37",
#     "client": "Home Office",
#     "trainer": {
#         "name": "David Harvey",
#         "energy_levels": "low"
#     }
# }
#
# print(data_eng_37, type(data_eng_37))
#
# print(data_eng_37["client"]) # DICTIONARY [KEY]
#
# data_eng_37["trainer"] = "David Harvey"
# data_eng_37["trainees"] = ["Munir", "Darnell", "Abhiram", "Ahmed"]
#
# print(data_eng_37)
#
# print(data_eng_37["trainer"][2])
#
# # print(data_eng_37.get("missing_key")) # Return None
# # print(data_eng_37["missing_key"]) # Fail noisily with error
#
# print(bool(data_eng_37.get("is this key here?")))
# data_eng_37.update({"course length": "8 weeks"})
# print(data_eng_37)

favourite_tv_show = {
    "show_name": "My Wife and Kids",
    "genre": "Sitcom",
    "main_actor": {
        "name": "Damon Wayans",
        "character_name": "Michael Kyle Sr.",
        "age": 61
    },
    "number_of_series": 5,
    "production": {
        "current_name": "ABC",
        "previous_name": "Touchstone"
           },
    "start_year": 2005
    }

print(favourite_tv_show)

print(favourite_tv_show["number_of_series"])

print(favourite_tv_show["main_actor"]["age"])

print(favourite_tv_show["production"]["current_name"])

print(favourite_tv_show.keys())
print(favourite_tv_show.values())
print(favourite_tv_show.items())

print(f"Abhi's favourite show is {favourite_tv_show['show_name']}. It has a start year of {favourite_tv_show['start_year']}")

