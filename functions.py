import requests
import json

def postcode_info(postcode):
    post_codes = requests.get(f"http://api.postcodes.io/postcodes/{postcode}".lower().strip())
    post_code_dict = post_codes.json()
    return post_code_dict['result']

def write_postcode_info_to_text(postcode):
    try:
        with open('postcode_info.txt', 'w') as outfile:
            json.dump(postcode_info(postcode), outfile)

    except FileNotFoundError:
        print('File not found')