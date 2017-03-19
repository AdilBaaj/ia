from flask_restful import Resource
from flask_restful import reqparse
from game.fight import Game
import simplejson as json

class SquareController(Resource):

    def get(self):
        from api import db
        from models import Square
        square = Square.query.first()
        hydratedSquare = {
            'x': square.x,
            'y': square.y,
            'nb': square.nb,
            'species': square.species
        }
        return hydratedSquare

    def post(self):
        from api import db
        from models import Square
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
                filter(Square.x==xAttackedSquare).\
                filter(Square.y==yAttackedSquare).first()

            game = Game(attackingSpecies, attackedSquare.species, nbAttackingSpecies, attackedSquare.nb)
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
