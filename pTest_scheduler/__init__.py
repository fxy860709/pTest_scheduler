# Bundle all above sections and expose the Flask APP

from flask import Flask

def create_app():
    app = Flask(__name__)
    return app
