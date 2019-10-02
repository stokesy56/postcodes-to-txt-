import requests

def postcode_info(postcode):
    post_codes = requests.get(f"http://api.postcodes.io/postcodes/{postcode}".lower().strip())
    post_code_dict = post_codes.json()
    return post_code_dict['result']

