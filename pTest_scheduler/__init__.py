# Bundle all above sections and expose the Flask APP

from flask import Flask

from .views.penv import penv
from .views.parse_json import parse_json
from .views.analysis_log import analysis_log
from .views.task import task
from .views.case import case


def create_app():
    app = Flask(__name__, template_folder='templates')

    # app = Flask(__name__)

    @app.route('/index')
    def index():
        return 'index'

    app.register_blueprint(penv)
    app.register_blueprint(task)
    app.register_blueprint(case)


    # app.register_blueprint(parse_json)
    # app.register_blueprint(analysis_log)

    return app
