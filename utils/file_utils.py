# utils/file_utils.py

import os
import json

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_json_to_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

def read_json_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)
