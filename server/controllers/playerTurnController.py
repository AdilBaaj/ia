from flask_restful import Resource
from game.constants import Species


class PlayerTurnController(Resource):

    def get(self):
        from api import db
        from models import PlayerTurn

        try:
            player = db.session.query(PlayerTurn).first()
            if player.turn:
                return {'turn': Species.VAMPIRE}
            else:
                return {'turn': Species.WEREWOLF}
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}

    def put(self):
        from api import db
        from models import PlayerTurn

        try:
            player = db.session.query(PlayerTurn).first()
            player.turn = not player.turn
            db.session.commit()
            if player.turn:
                return {'turn': Species.VAMPIRE}
            else:
                return {'turn': Species.WEREWOLF}
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}
