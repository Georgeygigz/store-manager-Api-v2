# app/__init__.py
'''
Register Blueprints
'''
from flask import Flask, Blueprint
from flask_restful import Api
from flask_jwt_extended import JWTManager
from datetime import timedelta


# local imports
from instance.config import app_configuration
from app.store_database import create_table, destory
from app.api.v2.views.store_views import (
    ViewProducts, ViewSingleProduct, ViewSalesRecord, SingleSale, ProductCategories, SinleProductCategory)
from app.api.v2.views.auth_view import CreateAccount, Login

blueprint = Blueprint('product', __name__, url_prefix='/api/v2')
app_api = Api(blueprint)


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_configuration['development'])
    app.register_blueprint(blueprint)
    app.config['JWT_SECRET_KEY'] = "vch37fhdser20rdbsk"
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=72)
    jwt = JWTManager(app)
    create_table()
    app_api.add_resource(ViewProducts, '/products')
    app_api.add_resource(ViewSingleProduct, '/products/<int:product_id>')
    app_api.add_resource(ViewSalesRecord, '/sales')
    app_api.add_resource(SingleSale, '/sales/<int:sale_id>')
    app_api.add_resource(ProductCategories, '/category')
    app_api.add_resource(SinleProductCategory, '/category/<int:category_id>')
    app_api.add_resource(CreateAccount, '/auth/register')
    app_api.add_resource(Login, '/auth/login')
    return app
