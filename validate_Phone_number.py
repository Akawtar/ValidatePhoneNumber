import json
import re

def validate_phone_number(phone_number, country_code):
    # Open the JSON file
    with open('Phone numbers.json', 'r') as json_file:
        # Load the contents of the file
        phone_formats = json.load(json_file)
    
    match_ = re.match(phone_formats[country_code], phone_number)
    if match_:
        return 'ok'
    return

# Example usage
phone_number = "080-1234-5678"  # Phone number to validate
country_code = "JP"  # Country code (e.g., US, GB, IN)

phone_number = re.findall(r'\d+', phone_number)
phone_number = ''.join(phone_number)


is_valid = validate_phone_number(phone_number, country_code)
if is_valid:
    print("Phone number is valid.")
else:
    print("Phone number is not valid.")
