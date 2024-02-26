from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()

# Sqlite
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '*p4$$w0rd*'

    # Sql Server
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://TulipAppLogin:T$l1p4pp!0g1n@localhost/Tulip?driver=ODBC+Driver+17+for+SQL+Server'

    # Sqlite
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Image, Like, Download, Tag, ImageTag, Color

    # sqlite
    # create_database(app)

    return app

# Sqlite
def create_database(app):
    if not path.exists('website' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Database Created!')
