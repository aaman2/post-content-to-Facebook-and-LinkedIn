from flask import Flask
from .config import Config
from .routes import main
from .oauth import oauth

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(oauth)

    return app
