import psycopg2
import os
from app.api.v2.models.store_model import Users
from dbconn import create_tables
from instance.config import app_configuration

dev_url = app_configuration['development'].DATA_BASE_URI


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(dev_url)
        self.curr = self.conn.cursor()

    def create_table(self):
        try:
            for query in create_tables:
                self.curr.execute(query)
            self.conn.commit()
            attedant = Users()
            attedant.insert_new_user(
                1,
                'george',
                "georgey@gmail.com",
                "$5$rounds=535000$c1lBmoZ/ffpmu0.7$XcIpRoAllo8dhF.o95k9f69lBxpSez8c9KduCvhBk68",
                "attedant")
            admin = Users()
            admin.insert_new_user(
                2,
                'mary',
                "mary@gmail.com",
                "$5$rounds=535000$c1lBmoZ/ffpmu0.7$XcIpRoAllo8dhF.o95k9f69lBxpSez8c9KduCvhBk68",
                "admin")
            self.curr.close
        except (Exception, psycopg2.DatabaseError) as e:
            return e

    ''' Destroying the tables'''

    def destory(self):
        products = "DROP TABLE IF EXISTS  products CASCADE"
        sales = "DROP TABLE IF EXISTS  sales CASCADE"
        users = "DROP TABLE IF EXISTS  users CASCADE"
        product_category = "DROP TABLE IF EXISTS  products_category CASCADE"
        drop_queries = [products, sales, users, product_category]
        try:
            for query in drop_queries:
                self.curr.execute(query)
            self.conn.commit()
            self.conn.close
        except Exception as e:
            return e


if __name__ == '__main__':
    Database().destory()
    Database().create_table()
