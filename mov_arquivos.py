import os
import shutil

#definir o caminho da pasta de origem e destino:

pasta_origem = "C:/Users/Fernando/Downloads"
pasta_destino = "C:/Users/Fernando/Downloads/pdf"

#Verifica se um arquivo ou diretorio existe
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)
    


#lista todos os arquivos na pasta de origem
arquivos = os.listdir(pasta_origem)

#filtra os aquivos com .pdf

arquivos_pdf = [arquivo for arquivo in arquivos if arquivo.lower().endswith(".pdf")]
print(arquivos_pdf)
#move os arquivo para pasta destino

for arquivo_pdf in arquivos_pdf:
    caminho_arquivo_origem = os.path.join(pasta_origem, arquivo_pdf)
    caminho_arquivo_destino = os.path.join(pasta_destino,arquivo_pdf)
    shutil.move(caminho_arquivo_origem, caminho_arquivo_destino)

print("arquivos movidos com sucesso!")

