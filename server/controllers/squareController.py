from flask_restful import Resource
from flask_restful import reqparse
from flask import abort
from game.fight import Game
from game.check_authorized_movement import check_if_authorized_movement
import json


class SquareController(Resource):

    @staticmethod
    def get_fight_result(nbAttackingSpecies, attackingSpecies, attackedSquare):
        # is_movement_authorized = check_if_authorized_movement(nbAttackingSpecies, attackingSpecies, attackedSquare)
        is_movement_authorized = True
        if is_movement_authorized:
            game = Game(attackingSpecies, attackedSquare.species, nbAttackingSpecies, attackedSquare.nb)
            fightResult = game.fightOrMerge()
            return fightResult['winningSpecies'], fightResult['nbWinningSpecies']
        else:
            abort(401, {'message': 'Movement not authorized'})

    @staticmethod
    def get():
        from models import Square
        squares = Square.query.all()
        hydrated_squares = []
        for square in squares:
            hydrated_squares = {
                'x': square.x,
                'y': square.y,
                'nb': square.nb,
                'species': square.species
            }
            hydrated_squares.append(hydrated_squares)
        return hydrated_squares

    def post(self):
        from api import db
        from models import Square
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('squares', action='append')
            args = parser.parse_args()
            attacked_squares = args['squares']
            attacking_species = args['species']
            for i in range(len(attacked_squares)):
                square = attacked_squares[i]
                square = json.loads(square.replace("'", '"'))
                x_attacked_square = square['x']
                y_attacked_square = square['y']
                nb_attacking_species = square['nb']

                attacked_square = db.session.query(Square).\
                    filter(Square.x == x_attacked_square).\
                    filter(Square.y == y_attacked_square).first()

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
