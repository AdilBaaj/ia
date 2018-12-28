from flask_restful import Resource
from flask_restful import reqparse
from flask import abort
from game.fight import Game
from game.check_authorized_movement import check_if_authorized_movement
import json


class SquareController(Resource):

    def get_fight_result(self, xAttackedSquare, yAttackedSquare, nbAttackingSpecies, attackingSpecies, attackedSquare):
        is_movement_authorized = check_if_authorized_movement(nbAttackingSpecies, attackingSpecies, attackedSquare)
        if is_movement_authorized:
            game = Game(attackingSpecies, attackedSquare.species, nbAttackingSpecies, attackedSquare.nb)
            fightResult = game.fightOrMerge()
            return fightResult['winningSpecies'], fightResult['nbWinningSpecies']
        else:
            abort(401, {'message': 'Movement not authorized'})

    def get(self):
        from models import Square
        squares = Square.query.all()
        hydratedSquares = []
        for square in squares:
            hydratedSquare = {
                'x': square.x,
                'y': square.y,
                'nb': square.nb,
                'species': square.species
            }
            hydratedSquares.append(hydratedSquare)
        return hydratedSquares

    def post(self):
        from api import db
        from models import Square
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('squares', action='append')
            parser.add_argument('species')
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
                    x_attacked_square,
                    y_attacked_square,
                    nb_attacking_species,
                    attacking_species,
                    attacked_square
                )
                db.session.commit()
                return {'x': args['x'], 'y': args['y'], 'nb': args['nb'], 'species': args['species']}

        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}
