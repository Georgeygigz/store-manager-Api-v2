import psycopg2
import os

from dbconn import create_tables
class Database:
    def __init__(self):
        self.conn=psycopg2.connect(os.getenv("DATABASE_URl"))
        self.curr=self.conn.cursor()


    def create_table(self):
        try:
            for query in create_tables:
                self.curr.execute(query)
            self.conn.commit()
            self.curr.close
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)

    ''' Destroying the tables'''
    def destory(self):
        products="DROP TABLE IF EXISTS  products CASCADE"
        sales="DROP TABLE IF EXISTS  sales CASCADE"
        users="DROP TABLE IF EXISTS  users CASCADE"
        product_category="DROP TABLE IF EXISTS  products_category CASCADE"
        drop_queries=[products,sales,users,product_category]
        try:
            for query in drop_queries:
                self.curr.execute(query)
            self.conn.commit()
            self.conn.close
        except Exception as e:
            print(e)


if __name__ == '__main__':
    Database().destory()
    Database().create_table()

