from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from app.api.v3.models.databases import db
from app.api.v3.models.auth_modles import User
from app.api.v3.models.products_model import Products
from app.api.v3.models.categories_model import Categories
from app.api.v3.models.sales_model import Sales

from instance.config import AppConfig
app = create_app(AppConfig)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()