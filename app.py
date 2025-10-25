from flask import Flask, jsonify, request, session
import sqlite3, os

app = Flask(__name__, static_folder='static', static_url_path='')
app.secret_key = 'chave_super_secreta'  # troque por algo seguro

DB = 'biblioteca.db'

# ---- Função de conexão ---- #
def conectar():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

# ---- Rotas ---- #

@app.route('/')
def index():
    return app.send_static_file('index.html')

# --- Login e logout --- #
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    senha = data.get('senha')

    # login simples
    if usuario == 'admin' and senha == '1234':
        session['usuario'] = usuario
        return jsonify({'mensagem': 'Login realizado com sucesso!'})
    else:
        return jsonify({'erro': 'Usuário ou senha incorretos'}), 401

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return jsonify({'mensagem': 'Logout realizado'})

# ---- API de livros ---- #
@app.route('/api/livros', methods=['GET'])
def listar_livros():
    if 'usuario' not in session:
        return jsonify({'erro': 'Não autorizado'}), 403

    busca = request.args.get('busca', '')
    conn = conectar()
    cur = conn.cursor()
    if busca:
        cur.execute("SELECT * FROM livros WHERE titulo LIKE ?", ('%' + busca + '%',))
    else:
        cur.execute("SELECT * FROM livros")
    livros = [dict(row) for row in cur.fetchall()]
    conn.close()
    return jsonify(livros)

@app.route('/api/livros', methods=['POST'])
def adicionar_livro():
    if 'usuario' not in session:
        return jsonify({'erro': 'Não autorizado'}), 403

    data = request.get_json()
    if not data or 'titulo' not in data:
        return jsonify({'erro': 'Título é obrigatório'}), 400

    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)",
                (data['titulo'], data.get('autor', ''), data.get('ano')))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Livro adicionado com sucesso!'})

@app.route('/api/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    if 'usuario' not in session:
        return jsonify({'erro': 'Não autorizado'}), 403

    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM livros WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Livro removido com sucesso!'})

# ---- Inicialização ---- #
if __name__ == '__main__':
    if not os.path.exists(DB):
        print("Banco não encontrado. Rode init_db.py primeiro.")
    app.run(debug=True)
