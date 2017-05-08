from flask_restful import Resource
from flask_restful import reqparse
from game.fight import Game
from game import constants


class SquareController(Resource):

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
        from models import Square, PlayerTurn
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('x', type=str, help='x')
            parser.add_argument('y', type=str, help='y')
            parser.add_argument('nb', type=str, help='Number')
            parser.add_argument('species', type=str, help='Species')

            args = parser.parse_args()
            xAttackedSquare = args['x']
            yAttackedSquare = args['y']
            nbAttackingSpecies = args['nb']
            attackingSpecies = args['species']

            attackedSquare = db.session.query(Square).\
                filter(Square.x == xAttackedSquare).\
                filter(Square.y == yAttackedSquare).first()
            if attackedSquare is None:
                attackedSquare = {}
                attackedSquare['species'] = constants.EMPTY
                attackedSquare['nb'] = 0

            game = Game(attackingSpecies, attackedSquare.species, nbAttackingSpecies, attackedSquare.nb)
            fightResult = game.fightOrMerge()
            square = Square(xAttackedSquare, yAttackedSquare, fightResult['nbWinningSpecies'], fightResult['winningSpecies'])

            if attackedSquare is not None:
                db.session.delete(attackedSquare)
            db.session.add(square)
            return {'x': args['x'], 'y': args['y'], 'nb': args['nb'], 'species': args['species']}

        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}

    def put(self):
        return {"response": "hello put"}

    def delete(self):
        return {"response": "hello delete"}
