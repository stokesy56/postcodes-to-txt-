import requests
import json

def postcode_info(postcode):
    try:
        post_codes = requests.get(f"http://api.postcodes.io/postcodes/{postcode}".lower().strip())
        post_code_dict = post_codes.json()
        return post_code_dict['result']
    except KeyError:
        return 'The URL entered is invalid. Please enter a valid UK postcode'

def write_postcode_info_to_text(file, postcode):
    if postcode_info(postcode) != 'The URL entered is invalid. Please enter a valid UK postcode':
        try:
            with open(file, 'w') as outfile:
                json.dump(postcode_info(postcode), outfile)
                return f'The postcode info has been added to {file}'
        except FileNotFoundError:
            return 'File not found'
    else:
        return postcode_info(postcode)