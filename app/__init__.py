# app/__init__.py
'''
Register Blueprints
'''
from flask import Flask, Blueprint,make_response,jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from datetime import timedelta
from app.api.v2.models.store_model import Users
import os
from instance.config import app_configuration, Config
from flask_cors import CORS

# local imports
from manage import Database
db=Database()
db.create_table()
           
from instance.config import app_configuration
from app.api.v2.views.store_views import (
    ViewProducts, ViewSingleProduct, ViewSalesRecord, SingleAttedantSales,
    SingleSale, ProductCategories, SingleProductCategory)
from app.api.v2.views.auth_view import CreateAccount, Login,SingleUser, Logout


blueprint = Blueprint('product', __name__, url_prefix='/api/v2')
app_api = Api(blueprint)
jwt = JWTManager()
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_configuration[config_name])
    app.register_blueprint(blueprint)
    app.config['JWT_SECRET_KEY'] = "dbskbjdmsdscdscdsdk"
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)
    jwt.init_app(app)
    CORS(app)
    app_api.add_resource(ViewProducts, '/products')
    app_api.add_resource(ViewSingleProduct, '/products/<int:product_id>')
    app_api.add_resource(ViewSalesRecord, '/sales')
    app_api.add_resource(SingleSale, '/sales/<int:sale_id>')
    app_api.add_resource(SingleAttedantSales, '/sales/<string:attedant_name>')
    app_api.add_resource(ProductCategories, '/category')
    app_api.add_resource(SingleProductCategory, '/category/<int:category_id>')
    app_api.add_resource(CreateAccount, '/auth/register')
    app_api.add_resource(Login, '/auth/login')
    app_api.add_resource(SingleUser, '/auth/user/<int:user_id>')
    app_api.add_resource(Logout, '/auth/logout')
    
    @app.errorhandler(404)
    def not_found(e):
        # defining function
        return make_response(jsonify({
            "Message": "Route not found. Please check on the route"
        }), 404)

    @app.errorhandler(500)
    def internal_error(e):
        return make_response(jsonify({
            "Message": "Internal server"
        }), 500)
    return app
