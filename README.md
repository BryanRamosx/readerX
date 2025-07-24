# readerX

# 📝 Editor de Arquivos com Interface Gráfica (Tkinter)

Este é um editor de arquivos com interface gráfica desenvolvido em **Python** utilizando a biblioteca **Tkinter**. O programa permite **abrir, visualizar e editar arquivos JSON e CSV**, além de **ler arquivos PDF**.

## 📌 Funcionalidades

- 📂 Abrir arquivos:
  - JSON (`.json`)
  - CSV (`.csv`)
  - PDF (`.pdf`) *(somente leitura)*
  
- ✏️ Editar o conteúdo dos arquivos JSON e CSV diretamente na interface.

- 💾 Salvar as alterações feitas.

- 🧾 Leitura de arquivos PDF com extração de texto (página por página).

## 🖥️ Interface

- Criada com o módulo `tkinter`.
- Área de texto com rolagem (`ScrolledText`) para exibir e editar conteúdo.
- Botões para abrir arquivos e salvar alterações.

## 📷 Captura de Tela


<img width="1906" height="986" alt="2025-07-23_22-44-47" src="https://github.com/user-attachments/assets/003f8d9f-441a-4c36-84f5-fd984691ee76" />

## ⚙️ Requisitos

- Python 3.7 ou superior

### Bibliotecas utilizadas:

- `tkinter` (inclusa no Python)
- `json` (inclusa no Python)
- `csv` (inclusa no Python)
- `PyPDF2`  
  Instale com:

  ```bash
  pip install PyPDF2
