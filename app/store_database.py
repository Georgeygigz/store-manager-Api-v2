import psycopg2
import os
from app.dbconn import create_tables
db_url=os.getenv("DATABASE_URL")



def conn_db():
	try:
		conn=psycopg2.connect(db_url)
	except Exception as e:
		raise e
	return conn

def create_table():
	conn=conn_db()
	curr=conn.cursor()
	try:
		for query in create_tables:
			curr.execute(query)
		conn.commit()
	except Exception as e:
		print(e)


def destory():
	conn =conn_db()
	curr=conn.cursor()
	orders="DROP TABLE IF EXISTS  products CASCADE"
	meals="DROP TABLE IF EXISTS  sales CASCADE"
	users="DROP TABLE IF EXISTS  users CASCADE"
	drop_queries=[orders,meals,users]
	try:
		for query in drop_queries:
			curr.execute(query)
		conn.commit()
	except Exception as e:
		print(e)


