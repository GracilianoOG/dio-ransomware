import pyaes
import os

def get_file_data(file_name):
    file = open(file_name, "rb")
    data = file.read()
    file.close()
    return data

def create_cipher(key_string):
    key = key_string.encode()
    return pyaes.AESModeOfOperationCTR(key)

def remove_file(file_name):
    os.remove(file_name)

def save_changed_file(file_name, data):
    new_file = file_name
    new_file = open(f"{new_file}", "wb")
    new_file.write(data)
    new_file.close()