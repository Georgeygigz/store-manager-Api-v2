#dbconn.py

'''Creates a connection to the store_manager database '''
import psycopg2
import os
url=os.getenv("DATABASE_URL")
try:
	conn=psycopg2.connect(url)
	curr=conn.cursor()

except Exception as e:
	print(e)

'''Creates the tables scripts '''         

table_1="""CREATE TABLE IF NOT EXISTS products(
                       product_id INT,
 	                   product_name VARCHAR PRIMARY KEY NOT NULL ,
 	                   category_id VARCHAR NOT NULL,
 	                   stock_amount INT NOT NULL,
 	                   price FLOAT,
 	                   low_inventory_stock INT);"""

table_2="""CREATE TABLE IF NOT EXISTS sales(
 	                    sale_id INT PRIMARY KEY,
 	                    attedant_name VARCHAR NOT NULL ,
 	                    customer_name VARCHAR NOT NULL,
 	                    product_name VARCHAR NOT NULL,
 	                    product_price FLOAT NOT NULL,
 	                    quantity FLOAT NOT NULL,
 	                    total_price FLOAT NOT NULL,
 	                    date_sold DATE);"""


table_3="""CREATE TABLE IF NOT EXISTS users(
 	                   user_id INT ,
 	                   username VARCHAR UNIQUE NOT NULL,
 	                   email VARCHAR NOT NULL PRIMARY KEY,
 	                   password VARCHAR NOT NULL,
 	                   user_type VARCHAR NOT NULL);"""

table_4="""CREATE TABLE IF NOT EXISTS products_category(
 	                   category_id INT ,
 	                   category_name VARCHAR PRIMARY KEY NOT NULL);"""

create_tables=[table_1,table_2,table_3,table_4]
