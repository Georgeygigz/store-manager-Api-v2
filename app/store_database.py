#store_database.py
'''Create new connection'''
import psycopg2
import os
from instance.config import app_configuration

'''Create a new connection '''
def conn_db():
	DATABASE_URL = os.environ['DATABASE_URL']
	conn = psycopg2.connect(DATABASE_URL, sslmode='require')
	return conn
