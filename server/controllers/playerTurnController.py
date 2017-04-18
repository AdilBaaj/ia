from flask_restful import Resource
from flask_restful import reqparse
from game.fight import Game
from game import constants
import simplejson as json

class PlayerTurnController(Resource):

    def get(self):
        return {"response" : "hello get"}

    def put(self):
        from api import db
        from models import PlayerTurn
        from game import constants

        try:
            player = db.session.query(PlayerTurn).first()
            player.turn = not player.turn
            db.session.commit()
            if player.turn == True:
                return '<{} turn>'.format(constants.MAP_SPECIES[int(constants.VAMPIRE)])
            else :
                return '<{} turn>'.format(constants.MAP_SPECIES[int(constants.WEREWOLF)])
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}

    def post(self):
        return {"response" : "hello post"}

    def delete(self):
        return {"response" : "hello delete"}
