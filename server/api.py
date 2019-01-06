from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('./flask_config.py')

api = Api(app)
db = SQLAlchemy(app)

# Do not move these imports from here
from models import *
from controllers import squareController, partyController, playerTurnController

migrate = Migrate(app, db)

api.add_resource(squareController.SquareController, '/api/square')
api.add_resource(partyController.PartyController, '/api/party')
api.add_resource(playerTurnController.PlayerTurnController, '/api/turn')

if __name__ == '__main__':
  app.run(
      host='0.0.0.0',
      port=5000,
      debug=True
  )
