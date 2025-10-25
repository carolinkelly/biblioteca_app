ESTRUTURA

biblioteca/
│
├─ app.py             # Seu servidor Flask   
├─ biblioteca.db      # Banco SQLite
├─ init_db.py         # Script para criar o banco
├─ requirements.txt   # Dependências do projeto
└─ static/
   └─ index.html      # Seu HTML atualizado

PASSO A PASSO
- verifique se o python está instalado 
  terminal:
  python --version

- instale o flask
  terminal:
  python3 -m pip install flask

- crie ambiente virtual
  terminal:
  python -m venv venv

- ative ambiente virtual
- terminal:
  venv\Scripts\activate

  --> RODAR em:
  http://127.0.0.1:5000



atualize o arquivo
pip freeze > requirements.txt
