import os
import shutil

# Defina o caminho da pasta de origem
pasta_origem = "C:/Users/Fernando/Downloads"

# Lista todos os itens (arquivos e diretórios) na pasta de origem
itens = os.listdir(pasta_origem)

# Cria um conjunto para armazenar extensões únicas
extensoes_unicas = set()

# Identifica as extensões únicas dos arquivos
for item in itens:
    if os.path.isfile(os.path.join(pasta_origem, item)):
        nome_arquivo, extensao = os.path.splitext(item)
        extensao = extensao.lower()
        extensoes_unicas.add(extensao)

# Cria pastas para as extensões únicas, se ainda não existirem
for extensao in extensoes_unicas:
    pasta_destino = os.path.join(pasta_origem, extensao[1:])  # Remove o ponto da extensão
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

# Move os arquivos para as pastas correspondentes
for item in itens:
    if os.path.isfile(os.path.join(pasta_origem, item)):
        nome_arquivo, extensao = os.path.splitext(item)
        extensao = extensao.lower()
        pasta_destino = os.path.join(pasta_origem, extensao[1:])
        
        caminho_arquivo_origem = os.path.join(pasta_origem, item)
        caminho_arquivo_destino = os.path.join(pasta_destino, item)
        
        shutil.move(caminho_arquivo_origem, caminho_arquivo_destino)
        print(f"Arquivo '{item}' movido para '{pasta_destino}'")

print("Movimentação de arquivos concluída!")
