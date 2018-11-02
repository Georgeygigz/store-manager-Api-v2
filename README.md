# store-manager-Api-v2
This is a Store Manager Web Application

[![Build Status](https://travis-ci.com/Georgeygigz/store-manager-Api-v2.svg?branch=bg-validation-161636257)](https://travis-ci.com/Georgeygigz/store-manager-Api-v2) [![Coverage Status](https://coveralls.io/repos/github/Georgeygigz/store-manager-Api-v2/badge.svg?branch=develop)](https://coveralls.io/github/Georgeygigz/store-manager-Api-v2?branch=develop)  [![Maintainability](https://api.codeclimate.com/v1/badges/d115bdb3f1e5b48e8d4e/maintainability)](https://codeclimate.com/github/Georgeygigz/store-manager-Api-v2/maintainability)

# This challenge creates a set of API Endpoints listed below
| EndPoints       | Functionality  | HTTP Method  |
| ------------- |:-------------:| -----:|
| api/v2/products | Get all the products| GET |
| api/v2/products/<int:product_id> | Fetch single product |GET|
| api/v2/products |Add a new product |POST|
| api/v2/products/<int:product_id> |Update product |PUT|
| api/v2/products/<int:product_id> |Delete product |DELETE|
| api/v2/products |Fetch all product |GET|
| api/v2/sales|New sale record |POST|
| api/v2/category|Get product category|GET|
| api/v2/category|Add a product category|POST|
| api/v2/category/<int:category_id>|Update product category|PUT|
| api/v2/category/<int:category_id>|Delete product category|DELETE|
| api/v2/auth/register|Create user account|POST|
| api/v2/auth/login|User login |POST|
| api/v2/auth/role|Update user role login |PUT|

## TOOLS TO BE USED IN THE CHALLENGE
1. Server-Side Framework:[Flask Python Framework](http://flask.pocoo.org/)
2. Linting Library:[Pylint, a Python Linting Library](https://www.pylint.org/)
3. Style Guide:[PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
4. Testing Framework:[PyTest, a Python Testing Framework](https://docs.pytest.org/en/latest/)
5. Testing Endpoints: [PostMan](https://www.getpostman.com/)

**How to run the application**
 1. Make a new directory on your computer
 2. Open the terminal and navigate to the folder
 3. `git clone` this  <code>[repo](https://github.com/Georgeygigz/store-manager-api/)</code>
 4.  run `pip install -r requirements.txt` to install the dependencies
 5.  Create a virtal environment
 5.  Export the environmental variable
 5.  Then on your terminal write ```flask run``` to start the server
 6. Then on [postman](https://www.getpostman.com/), navigate to this url `api/v2/auth/login`


# heroku application Link

 Navigate to this [link](https://storemanagerv2.herokuapp.com/api/v2/login) to run my application on heroku

 # View on postman documentation
 Postman documentation[link](https://documenter.getpostman.com/view/5283750/RzZ4pMf1#8d58fbc0-3292-b080-fe59-a9c1c351026b)

# Author
`Georgey Gigz`

# Realease 
 Version one `(v2)`
