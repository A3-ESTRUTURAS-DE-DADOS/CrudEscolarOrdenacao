from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Instanciando as extensões do SQLAlchemy e do Migrate
db = SQLAlchemy()
migrate = Migrate()