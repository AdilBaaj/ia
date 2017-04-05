from flask import Flask
from flask_restful import Api
from controllers import squareController
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

@app.after_request

def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

db = SQLAlchemy(app)

api.add_resource(squareController.SquareController, '/api/square')

if __name__ == '__main__':
    app.run(debug=True)
