from flask import Flask
from .core.config import ensure_memory
from .routes import bp

def create_app():
    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False
    app.register_blueprint(bp)
    ensure_memory()
    return app
