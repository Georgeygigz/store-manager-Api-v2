#app/__init__.py
'''
Register Blueprints
'''
from flask import Flask,Blueprint
from flask_restful import Api


#local imports
from instance.config import app_configuration
from app.store_database import create_table, destory

blueprint=Blueprint('product',__name__,url_prefix='/api/v2')
app_api=Api(blueprint)
def create_app():
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_configuration['development'])
    app.register_blueprint(blueprint)
    create_table()
    return app
