import os
from controller import routes
from flask import Flask
from extensions import db, migrate, ma
from flask_assets import Environment, Bundle

app = Flask(__name__)

db.init_app(app)
migrate.init_app(app)
ma.init_app(app)

assets = Environment(app)
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run()