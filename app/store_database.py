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
