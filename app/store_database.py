#store_database.py

'''Create new tables in store_manager data base'''
import psycopg2
import os
from app.dbconn import create_tables
db_url=os.getenv("DATABASE_URL")


'''Create a new connection '''
def conn_db():
	try:
		conn=psycopg2.connect(db_url)
	except Exception as e:
		raise e
	return conn

''' Add the tables to store_manager database'''
def create_table():
	conn=conn_db()
	curr=conn.cursor()
	try:
		for query in create_tables:
			curr.execute(query)
		conn.commit()
	except Exception as e:
		print(e)

''' Destroying the tables'''
def destory():
	conn =conn_db()
	curr=conn.cursor()
	orders="DROP TABLE IF EXISTS  products CASCADE"
	meals="DROP TABLE IF EXISTS  sales CASCADE"
	users="DROP TABLE IF EXISTS  users CASCADE"
	product_category="DROP TABLE IF EXISTS  products_category CASCADE"
	drop_queries=[orders,meals,users,product_category]
	try:
		for query in drop_queries:
			curr.execute(query)
		conn.commit()
	except Exception as e:
		print(e)
