import requests
import json
from pprint import pprint

headers = {'Content-Type': 'application/json'}
body = {'postcodes': ["PR3 0SG", "M45 6GN", "EX165BL"]}

pc_req = requests.post(
    url="https://api.postcodes.io/postcodes/",
    headers=headers,
    data=json.dumps(body)
)

print(pc_req)
pcs = pc_req.json()['result']
print(pcs)

#admin_ward, easting, northings, NUTS code
for pc_data in pcs:
    result = pc_data['result']
    print('-----', result['postcode'], '-----')
    print('Admin Ward', result['admin_ward'])
    print('Eastings =', result['eastings'], ',', 'Northings = ', result['northings'])
    print('NUTS code =', result['codes']['nuts'])






# if pc_req.status_code == 200:
#     # pprint(dict(pc_req.headers), sort_dicts=False)
#     print(pc_req.content, type(pc_req.content))  # class = bytes
#     postcode = pc_req.json()
#     pprint(postcode)
#     result = postcode['result']
#     print(result['admin_district'])
#     print(result['eastings'])
#     print(result['northings'])
#     print(result['codes']['nuts'])

# print the admin_district, the eastings and northings, NUTS code