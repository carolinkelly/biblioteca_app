import sqlite3

# Conecta e cria o banco
conn = sqlite3.connect('biblioteca.db')
cur = conn.cursor()

# Cria tabela
cur.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT,
    ano INTEGER
)
''')



# 10 livros iniciais
livros = [
    ("Dom Casmurro", "Machado de Assis", 1899),
    ("O Alquimista", "Paulo Coelho", 1988),
    ("Capitães da Areia", "Jorge Amado", 1937),
    ("Vidas Secas", "Graciliano Ramos", 1938),
    ("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881),
    ("A Hora da Estrela", "Clarice Lispector", 1977),
    ("Grande Sertão: Veredas", "Guimarães Rosa", 1956),
    ("O Cortiço", "Aluísio Azevedo", 1890),
    ("Iracema", "José de Alencar", 1865),
    ("A Moreninha", "Joaquim Manuel de Macedo", 1844)
]

# Insere livros (só se tabela estiver vazia)
cur.executemany("INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)", livros)

conn.commit()
conn.close()

print("Banco criado com 10 livros iniciais!")

# --- Tabela de usuários ---
cur.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    email TEXT
)
''')

# Popula usuários de exemplo
usuarios = [
    ('aluno1', 'senha123', 'aluno1@email.com'),
    ('aluno2', 'senha456', 'aluno2@email.com')
]
cur.executemany('INSERT INTO usuarios (username, senha, email) VALUES (?, ?, ?)', usuarios)

conn.commit()
conn.close()

print("Banco e tabelas criados com sucesso!")
