import os
import pyaes

# Abre o arquivo criptografado
file_name = "teste.txt.encrypted"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# Gera a chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Descriptografa o arquivo
decrypted_data = aes.decrypt(file_data)

# Remove o arquivo criptografado
os.remove(file_name)

# Cria o arquivo descriptografado
new_file = "teste.txt"
new_file = open(f"{new_file}", "wb")
new_file.write(decrypted_data)
new_file.close()