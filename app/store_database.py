#store_database.py

'''Create new connection'''
import psycopg2
import os
from instance.config import app_configuration

config_name = os.getenv("APP_SETTINGS")
dev_url=app_configuration['development'].DATA_BASE_URL
test_url=app_configuration['testing'].DATABASE_URL


'''Create a new connection '''
def conn_db():
	try:
		if config_name=='testing':
			conn=psycopg2.connect(test_url)
		if config_name=='development':
			conn=psycopg2.connect(dev_url)			
	except Exception as e:
		return {"Message": e}
	return conn
