import json
import urllib
import string
from pprint import pprint 

# Reading JSON file
with open('data_input.json') as f:
    data = json.load(f)    

for data_item in data:
    fields = ['street_1','street_2','city','zip','state','country']

    # Replacing Null value with empty string 
    for field in fields:
        if data_item[field] is None:
            data_item[field] = ''
        else:
            continue

    # Concatinate Address fields
    checked_addr = data_item['street_1']+' '+data_item['street_2']+' '+data_item['city']+' '+data_item['zip']+' '+data_item['state']+' '+data_item['country']
    
    # Replacing special characters with empty string
    checked_addr = string.replace(checked_addr, '#', '')
    checked_addr = string.replace(checked_addr, '&', '')
    checked_addr = string.replace(checked_addr, '/', '')
    
    # Utilising HereMaps API to check if adress is Valid
    url = "https://geocoder.api.here.com/6.2/geocode.json?app_id=APP_ID&app_code=APP_CODE&searchtext="+checked_addr+""
    response_api = urllib.urlopen(url.encode('ascii','ignore'))
    data_api = json.loads(response_api.read())

    # Mark invalid addresses
    data_item['valid'] = bool(data_api['Response']['View'])

    # Mark Residential addresses
    data_item['is_residential'] = data_item['company'] is not None

    # Write to JSON
    with open('data_output.json', 'w') as outfile:
        json.dump(data, outfile)

    
