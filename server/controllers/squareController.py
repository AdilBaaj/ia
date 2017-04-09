from flask_restful import Resource
from flask_restful import reqparse
from game.fight import Game
import simplejson as json

class SquareController(Resource):

    def get(self):
        from api import db
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
            print(parser.__dict__)
            parser.add_argument('x', type=str, help='x')
            parser.add_argument('y', type=str, help='y')
            parser.add_argument('nb', type=str, help='Number')
            parser.add_argument('species', type=str, help='Species')

            args = parser.parse_args()
            print(args)
            xAttackedSquare = args['x']
            yAttackedSquare = args['y']
            nbAttackingSpecies = args['nb']
            attackingSpecies = args['species']

            print(xAttackedSquare)
            print(yAttackedSquare)
            print(nbAttackingSpecies)
            print(attackingSpecies)

            attackedSquare = db.session.query(Square).\
                filter(Square.x==xAttackedSquare).\
                filter(Square.y==yAttackedSquare).first()
            if attackedSquare is None:
                attackedSquare = {}
                attackedSquare['species'] = None
                attackedSquare['nb'] = None
            elif attackedSquare.species == attackingSpecies:
                attackedSquare.nb = int(nbAttackingSpecies) + int(attackedSquare.nb)
                db.session.commit()

                return {'x':args['x'], 'y': args['y'], 'nb': attackedSquare.nb, 'species': attackingSpecies}

            game = Game(attackingSpecies, attackedSquare['species'], nbAttackingSpecies, attackedSquare['nb'])
            fightResult = game.fight()
            print(fightResult)
            square = Square(xAttackedSquare, yAttackedSquare, fightResult['nbWinningSpecies'], fightResult['winningSpecies'])
            db.session.add(square)
            db.session.commit()

            return {'x': args['x'], 'y': args['y'], 'nb': args['nb'], 'species': args['species']}

        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}

    def put(self):
        return {"response" : "hello put"}

    def delete(self):
        return {"response" : "hello delete"}
