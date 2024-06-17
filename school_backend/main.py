import os
from flask import Flask
from config import Config
from extensions import db, migrate
from flask import Flask
from flask_cors import CORS

"""
Este é o arquivo principal da aplicação Flask. Ele é responsável por instanciar a aplicação,
configurar as extensões, importar as configurações e registrar as rotas.

CORS(app) habilita o CORS (Cross-Origin Resource Sharing), que é uma política de segurança da web que permite
recursos restritos em uma página da web a serem solicitados a partir de um domínio diferente daquele que serviu o recurso.

db.init_app(app) inicializa a extensão SQLAlchemy com a aplicação Flask.

migrate.init_app(app, db) inicializa a extensão Flask-Migrate com a aplicação Flask e a instância do banco de dados.

app.register_blueprint(routes) registra o blueprint contendo as rotas da aplicação.

app.run é usado para iniciar a aplicação Flask.

OBS: Este arquivo (main.py) deve ser executado para iniciar a aplicação.
"""

# Instancia a aplicação Flask
app = Flask(__name__)

# Carrega as configurações da aplicação a partir do objeto Config
app.config.from_object(Config)

# Habilita CORS na aplicação
CORS(app)

# Inicializa a extensão SQLAlchemy com a aplicação Flask
db.init_app(app)

# Inicializa a extensão Flask-Migrate com a aplicação Flask e o banco de dados
migrate.init_app(app, db)

# Importa e registra as rotas da aplicação
from app.routes import routes
app.register_blueprint(routes)

# Inicia a aplicação Flask se o arquivo for executado diretamente
if __name__ == '__main__':
    app.run(
        port=os.getenv('PORT', 5000),  # Configura a porta da aplicação a partir da variável de ambiente PORT (padrão: 5000)
        host=os.getenv('HOST', 'localhost')  # Configura o host da aplicação a partir da variável de ambiente HOST (padrão: localhost)
    )