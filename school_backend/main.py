import os
from flask import Flask
from config import Config
from extensions import db, migrate
from flask import Flask
from flask_cors import CORS

'''
Esse é o arquivo principal da aplicação do Flask, ele é responsável por instanciar a aplicação e as extensões do SQLAlchemy e do Migrate. 
Ele também importa as configurações da aplicação e as rotas da aplicação.

CORS(app) é usado para habilitar o CORS (uma política de segurança) na aplicação.
db.init_app(app) é usado para inicializar o SQLAlchemy com a aplicação.
migrate.init_app(app, db) é usado para inicializar o Migrate com a aplicação.
app.register_blueprint(routes) é usado para registrar as rotas da aplicação.
app.run é usado para rodar a aplicação.

OBS: o arquivo main.py é o arquivo que deve ser executado para iniciar a aplicação.
'''

app = Flask(__name__)

app.config.from_object(Config)

CORS(app)
db.init_app(app)
migrate.init_app(app, db)

from app.routes import routes

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(
        port=os.getenv('PORT', 5000),
        host=os.getenv('HOST', 'localhost')
    )