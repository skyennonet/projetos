import openpyxl
import tkinter as tk
from tkinter import filedialog, messagebox
import json

# Nome do arquivo de configuração para salvar a localização do arquivo XLSX
config_file = "config.json"

class ExcelSearchReplaceApp:
    def __init__(self):
        self.file_path = None
        self.load_config()

        self.root = tk.Tk()
        self.root.title("Pesquisa e Substituição de Itens em Excel")
        self.root.geometry("500x400")

        self.create_interface()

    def load_config(self):
        try:
            with open(config_file, "r") as f:
                config = json.load(f)
                self.file_path = config.get("file_path")
        except (FileNotFoundError, json.JSONDecodeError):
            self.file_path = None

    def save_config(self):
        config = {"file_path": self.file_path}
        with open(config_file, "w") as f:
            json.dump(config, f)

    def search_term_in_workbook(self, term_to_search, new_text):
        # Código de busca e substituição

        def perform_search(self):
            term_to_search = self.search_entry.get().lower()
            self.search_result_text.delete(1.0, tk.END)  # Limpa o resultado da busca anterior
            self.search_term_in_workbook(term_to_search, None)

    def replace_item(self):
        term_to_replace = self.search_entry.get().lower()
        new_text = self.new_text_entry.get()  # Obtém o novo texto do Entry correspondente
        self.search_result_text.delete(1.0, tk.END)  # Limpa o resultado da busca anterior
        if new_text:  # Verifica se o novo texto foi fornecido
            self.search_term_in_workbook(term_to_replace, new_text)
            self.save_config()  # Salva a configuração após a substituição
        else:
            messagebox.showinfo("Erro", "Digite o novo texto para realizar a substituição.")

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx")])
        if self.file_path:
            messagebox.showinfo("Sucesso", "Arquivo XLSX selecionado com sucesso!")
            self.save_config()

    def create_interface(self):
        search_frame = tk.Frame(self.root)
        search_frame.pack()

        search_label = tk.Label(search_frame, text="Digite a informação da impressora:")
        search_label.grid(row=0, column=0)

        self.search_entry = tk.Entry(search_frame, width=30)
        self.search_entry.grid(row=0, column=1)

        search_button = tk.Button(search_frame, text="Buscar", command=self.perform_search)
        search_button.grid(row=0, column=2)

        self.search_result_text = tk.Text(self.root, wrap=tk.WORD, width=60, height=10)
        self.search_result_text.pack()

        replace_frame = tk.Frame(self.root)
        replace_frame.pack()

        new_value_label = tk.Label(replace_frame, text="Insira o texto a ser substituído:")
        new_value_label.grid(row=0, column=0)

        self.new_value_entry = tk.Entry(replace_frame, width=30)
        self.new_value_entry.grid(row=0, column=1)

        new_text_label = tk.Label(replace_frame, text="Insira o novo texto:")
        new_text_label.grid(row=1, column=0)

        self.new_text_entry = tk.Entry(replace_frame, width=30)
        self.new_text_entry.grid(row=1, column=1)

        replace_button = tk.Button(self.root, text="Substituir Item", command=self.replace_item)
        replace_button.pack()

        file_button = tk.Button(self.root, text="Selecionar Arquivo", command=self.select_file)
        file_button.pack()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ExcelSearchReplaceApp()
    app.run()
