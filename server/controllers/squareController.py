from flask_restful import Resource
from flask_restful import reqparse
from flask import abort
from game.fight import Game
import json


class SquareController(Resource):

    @staticmethod
    def get_fight_result(nb_attacking_species, attacking_species, attacked_square):
        is_movement_authorized = True
        if is_movement_authorized:
            game = Game(attacking_species, attacked_square.species, nb_attacking_species, attacked_square.nb)
            fight_result = game.fightOrMerge()
            return fight_result['winningSpecies'], fight_result['nbWinningSpecies']
        else:
            abort(401, {'message': 'Movement not authorized'})

    @staticmethod
    def get():
        from models import Square
        squares = Square.query.all()
        list_dehydrated_squares = []
        for square in squares:
            dehydrated_square = {
                'x': square.x,
                'y': square.y,
                'nb': square.nb,
                'species': square.species
            }
            list_dehydrated_squares.append(dehydrated_square)
        return list_dehydrated_squares

    def post(self):
        from api import db
        from models import Square, PlayerTurn
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('squares', action='append')
            args = parser.parse_args()
            attacked_squares = args['squares']
            attacking_species = db.sessions.query(PlayerTurn).first()
            for i in range(len(attacked_squares)):
                square = attacked_squares[i]
                square = json.loads(square.replace("'", '"'))
                nb_attacking_species = square['nb']

                attacked_square = db.session.query(Square).\
                    filter(Square.x == square['x']).\
                    filter(Square.y == square['y']).first()

                attacked_square.species, attacked_square.nb = self.get_fight_result(
                    nb_attacking_species,
                    attacking_species,
                    attacked_square
                )
            db.session.commit()
            return 'Success'

        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}
