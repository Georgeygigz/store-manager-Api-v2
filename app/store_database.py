#store_database.py

'''Create new connection'''
import psycopg2
import os
config_name=os.getenv("APP_SETTINGS")
dev_url=os.getenv("DATABASE_URL")
test_url=os.getenv("TEST_DATABASE_URL")
release_url=os.getenv("RELEASE_DATABASE_URL")

'''Create a new connection '''
def conn_db():
	try:
		if config_name=='testing':
			conn=psycopg2.connect(dev_url)
		if config_name=='development':
			conn=psycopg2.connect(test_url)
		if config_name=='release':
			conn=psycopg2.connect(release_url)
			
	except Exception as e:
		raise e
	return conn
