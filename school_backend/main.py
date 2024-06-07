import os
from flask import Flask
from extensions import db, migrate, ma
from flask_assets import Environment, Bundle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.zpawzfahadpotbvyfnfh:postgres@123@aws-0-sa-east-1.pooler.supabase.com:6543/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app,db)
ma.init_app(app)

assets = Environment(app)

from controller.controller import routes
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run()
    
'''
- Fazer o front da tabela
- Fazer as rotas http (controller)
- Fazer as rotas para puxar da api
- Fazer as tabelas pelo flask (models)
- Angular (views)
'''