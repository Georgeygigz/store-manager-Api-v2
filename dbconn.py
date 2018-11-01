'''Creates the tables scripts '''

products = """CREATE TABLE IF NOT EXISTS products(
                       product_id INT,
 	                   product_name VARCHAR PRIMARY KEY NOT NULL ,
 	                   category_id VARCHAR NOT NULL,
 	                   stock_amount INT NOT NULL,
 	                   price FLOAT,
 	                   low_inventory_stock INT);"""

sales = """CREATE TABLE IF NOT EXISTS sales(
 	                    sale_id INT PRIMARY KEY,
 	                    attedant_name VARCHAR NOT NULL ,
 	                    customer_name VARCHAR NOT NULL,
 	                    product_name VARCHAR NOT NULL,
 	                    product_price FLOAT NOT NULL,
 	                    quantity FLOAT NOT NULL,
 	                    total_price FLOAT NOT NULL,
 	                    date_sold DATE);"""


users = """CREATE TABLE IF NOT EXISTS users(
 	                   user_id INT ,
 	                   username VARCHAR UNIQUE NOT NULL,
 	                   email VARCHAR NOT NULL PRIMARY KEY,
 	                   password VARCHAR NOT NULL,
 	                   user_type VARCHAR NOT NULL);"""

category = """CREATE TABLE IF NOT EXISTS products_category(
 	                   category_id INT ,
 	                   category_name VARCHAR PRIMARY KEY NOT NULL);"""

create_tables = [products, sales, users, category]
