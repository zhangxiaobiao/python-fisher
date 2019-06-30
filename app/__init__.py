"""
Created by snow at 2019/6/30 
"""
from flask import Flask

__author__ = 'snow'

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
