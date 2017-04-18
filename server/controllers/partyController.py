from flask_restful import Resource
from flask_restful import reqparse
from game.fight import Game
import simplejson as json

class PartyController(Resource):

    def get(self):
        return {"response" : "hello get"}

    # Creates a new board
    def post(self):
        from api import db
        from models import Square
        from game import constants
        try:
            num_rows_deleted = db.session.query(Square).delete()
            db.session.commit()
            boardHeight = 15
            boardWidth = 15

            for i in range(boardWidth):
                for j in range(boardHeight):
                    square = Square(i, j, None, 0)
                    db.session.add(square)
            db.session.commit()
            return "OK New Board"
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}

    def put(self):
        return {"response" : "hello put"}

    def delete(self):
        return {"response" : "hello delete"}
