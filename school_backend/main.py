import os
from flask import Flask
from config import Config
from extensions import db, migrate

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

from app.routes import routes

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(
        port=os.getenv('PORT', 5000),
        host=os.getenv('HOST', 'localhost')
    )