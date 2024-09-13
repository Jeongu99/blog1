from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(app.instance_path, 'blog.db')}"
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)

    migrate = Migrate(app, db)


    from . import routes
    app.register_blueprint(routes.bp)

    return app
