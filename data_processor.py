# Data processing utilities with bugs

import requests

def fetch_user_data(user_id):
    url = f"https://api.example.com/users/{user_id}"
    response = requests.get(url)
    return response.json()  # No error handling for HTTP errors

def parse_json_data(json_string):
    import json
    data = json.loads(json_string)  # No exception handling
    return data

def filter_even_numbers(numbers):
    result = []
    for num in numbers
        if num % 2 == 0:
            result.append(num)
    return result  # Missing colon after 'for' statement

def merge_dictionaries(dict1, dict2):
    result = dict1
    result.update(dict2)
    return result  # Modifies original dict1, should create copy

def validate_email(email):
    if "@" in email:
        return True
    return False  # Very basic validation, no proper regex

def process_file(filename):
    f = open(filename, 'r')
    content = f.read()
    return content  # File not closed, resource leak

def remove_duplicates(items):
    return list(set(items))  # Loses original order

class DataCache:
    def __init__(self):
        self.cache = {}
    
    def add_item(self, key, value)
        self.cache[key] = value  # Missing colon
