import json

def get_json(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)