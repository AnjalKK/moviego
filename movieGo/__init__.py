import os

from flask import Flask
from flask_bootstrap import Bootstrap5


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    bootstrap = Bootstrap5(app)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/hello')
    def hello():
        return 'Hello, World!!!!'

    from . import auth
    app.register_blueprint(auth.bp)

    from . import book
    app.register_blueprint(book.bp)

    return app

if __name__ == '__main__':
    app.run(debug=True, port=8001)