import pyaes
import os

def get_file_data(file_name):
    file = open(file_name, "rb")
    data = file.read()
    file.close()
    return data

def create_cipher(key_string):
    return pyaes.AESModeOfOperationCTR(key_string.encode())

def remove_file(file_name):
    os.remove(file_name)

def save_changed_file(file_name, data):
    file_name = open(f"{file_name}", "wb")
    file_name.write(data)
    file_name.close()