from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
SECRET_KEY = "some thing"  # your secret key


def create_note_app():
    app = Flask(__name__, template_folder="templates")

    # IMPORTANT: add this
    app.config["SECRET_KEY"] = SECRET_KEY
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from route import register_routes
    register_routes(app)

    return app
