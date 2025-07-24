import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import json
import csv
import PyPDF2

class FileEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Arquivos")
        self.root.geometry("600x400")

        # Variável para armazenar o caminho do arquivo
        self.file_path = None
        self.file_type = None  # 'json', 'csv' ou 'pdf'

        # Widgets da interface
        self.btn_open = tk.Button(root, text="Abrir Arquivo", command=self.open_file)
        self.btn_open.pack(pady=10)

        self.btn_save = tk.Button(root, text="Salvar Alterações", command=self.save_file, state=tk.DISABLED)
        self.btn_save.pack(pady=5)

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
        self.text_area.pack(padx=10, pady=10)

    def open_file(self):
        # Abre a janela de seleção de arquivo
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON Files", "*.json"), ("CSV Files", "*.csv"), ("PDF Files", "*.pdf")]
        )

        if not file_path:
            return

        self.file_path = file_path

        # Verifica o tipo do arquivo
        if file_path.endswith('.json'):
            self.file_type = 'json'
            self.load_json()
        elif file_path.endswith('.csv'):
            self.file_type = 'csv'
            self.load_csv()
        elif file_path.endswith('.pdf'):
            self.file_type = 'pdf'
            self.load_pdf()

        self.btn_save.config(state=tk.NORMAL)

    def load_json(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, json.dumps(data, indent=4))
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao ler o JSON: {e}")

    def load_csv(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                csv_data = list(reader)
                self.text_area.delete(1.0, tk.END)
                for row in csv_data:
                    self.text_area.insert(tk.END, ','.join(row) + '\n')
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao ler o CSV: {e}")

    def load_pdf(self):
        try:
            with open(self.file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n--- Página ---\n"
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, text)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao ler o PDF: {e}")

    def save_file(self):
        if not self.file_path:
            return

        try:
            if self.file_type == 'json':
                data = json.loads(self.text_area.get(1.0, tk.END))
                with open(self.file_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, indent=4)
            elif self.file_type == 'csv':
                text = self.text_area.get(1.0, tk.END)
                rows = [line.split(',') for line in text.split('\n') if line]
                with open(self.file_path, 'w', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
            else:
                messagebox.showinfo("Aviso", "PDF não pode ser editado neste exemplo.")
                return

            messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileEditorApp(root)
    root.mainloop()