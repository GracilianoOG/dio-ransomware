import utils

FILE_NAME = "teste.txt.encrypted"
KEY = "testeransomwares"

# Abre o arquivo criptografado
file_data = utils.get_file_data(FILE_NAME)

# Gera a chave para descriptografia
aes = utils.create_cipher("testeransomwares")

# Descriptografa o arquivo
decrypted_data = aes.decrypt(file_data)

# Remove o arquivo criptografado
utils.remove_file(FILE_NAME)

# Cria o arquivo descriptografado
utils.save_changed_file(FILE_NAME.replace(".encrypted", ""), decrypted_data)