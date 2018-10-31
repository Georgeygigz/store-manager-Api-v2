#store_database.py

'''Create new connection'''
import psycopg2
import os
db_url=os.getenv("DATABASE_URL")

'''Create a new connection '''
def conn_db():
	try:
		conn=psycopg2.connect(db_url)
	except Exception as e:
		raise e
	return conn
