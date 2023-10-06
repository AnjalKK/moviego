import os

from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/')
    def index():
        return render_template('landingpage.html')

    @app.route('/hello')
    def hello():
        return 'Hello, World!!!!'

    from . import auth
    app.register_blueprint(auth.bp)

    from . import book
    app.register_blueprint(book.bp)

    return app
