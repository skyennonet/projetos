import os
import shutil
import tkinter as tk
from tkinter import filedialog

def selecionar_pasta_origem():
    global pasta_origem
    pasta_origem = filedialog.askdirectory()
    pasta_origem_label.config(text=f"Pasta de Origem: {pasta_origem}")

def mover_arquivos():
    itens = os.listdir(pasta_origem)
    extensoes_unicas = set()

    for item in itens:
        if os.path.isfile(os.path.join(pasta_origem, item)):
            nome_arquivo, extensao = os.path.splitext(item)
            extensao = extensao.lower()
            extensoes_unicas.add(extensao)

    for extensao in extensoes_unicas:
        pasta_destino = os.path.join(pasta_origem, extensao[1:])
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

    for item in itens:
        if os.path.isfile(os.path.join(pasta_origem, item)):
            nome_arquivo, extensao = os.path.splitext(item)
            extensao = extensao.lower()
            pasta_destino = os.path.join(pasta_origem, extensao[1:])
        
            caminho_arquivo_origem = os.path.join(pasta_origem, item)
            caminho_arquivo_destino = os.path.join(pasta_destino, item)
        
            shutil.move(caminho_arquivo_origem, caminho_arquivo_destino)
            resultado_label.config(text=f"Arquivo '{item}' movido para '{pasta_destino}'")

# Cria a janela da interface
root = tk.Tk()
root.title("Movimentador de Arquivos")

# Botão para selecionar a pasta de origem
selecionar_botao = tk.Button(root, text="Selecionar Pasta de Origem", command=selecionar_pasta_origem)
selecionar_botao.pack()

# Label para exibir a pasta de origem selecionada
pasta_origem_label = tk.Label(root, text="Pasta de Origem: ")
pasta_origem_label.pack()

# Botão para iniciar o movimento dos arquivos
mover_botao = tk.Button(root, text="Mover Arquivos", command=mover_arquivos)
mover_botao.pack()

# Label para exibir resultados
resultado_label = tk.Label(root, text="")
resultado_label.pack()

# Inicia a interface gráfica
root.mainloop()
