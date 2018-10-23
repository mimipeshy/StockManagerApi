# Stock-Manager-Api         [![Build Status](https://travis-ci.org/mimipeshy/Stock-Manager-Api.svg?branch=master)](https://travis-ci.org/mimipeshy/Stock-Manager-Api)


Store Manager API is a flask RESTful API that helps store owners manage sales and product inventory records.The store owner or admin can:-

- Add products to the store
- Get a specific product 
- Get all products 
- Add sale records
- Get one specific sale 

## Getting Started

1) Clone the repository by doing: `git clone https://github.com/mimipeshy/Stock-Manager-Api.git`

2)Git checkout ch-integrate-with-travis-61405239

3) Create a virtual environment: `virtualenv env`

4) Activate the virtual environment: `source venv/bin/activate` on Linux/Mac  or `source venv/Scripts/activate` on windows.

5) Install the requirements : `pip install -r requirements.txt`


## Running tests
Use nosetest to run: `nosetests --exe --with-coverage --cover-package=app` 

### Prerequisites
-   python 3.6
-   virtual environment


## Running it on machine
- Create a .env file to store your environment variables: `touch .venv`
- In the `.venv` file add this line: `export SECRET=<your-secret-key-here`
- On terminal do: `source .venv`
- Run the application: `python run`
- The api endpoints can be consumed using postman.

## Endpoints
| Endpoint                                   | FUNCTIONALITY                      |
| ----------------------------------------   |:----------------------------------:|
| POST  /api/v1/products                     | This will add a product            |
| POST  /api/v1/sales                        | This will add a sale               | 
| GET  /api/v1/products                      | This will get all products         |
| GET  /api/v1/products/product_id           | retrieve a single product by id    |
| GET  /api/v1/sales                         | retrieve all sale records          |
| GET  /api/v1/sales/sale_id                 | retrieves a single sale record     | 

## Heroku application
https://store-manager-api-app-v1.herokuapp.com/

## Built With
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) -  The web framework used
* [Pip](https://pypi.python.org/pypi/pip) -  Dependency Management

## Authors
* **Peris Ndanu** 

## License

This project is licensed under the MIT Licens