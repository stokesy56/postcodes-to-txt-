import requests

def postcode_info(postcode)
    post_codes = requests.get("http://api.postcodes.io/postcodes/wd38hy")
    post_code_dict = post_codes.json()
    return post_code_dict['result']

