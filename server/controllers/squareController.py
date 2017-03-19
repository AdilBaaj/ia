from flask_restful import Resource
from flask_restful import reqparse


class SquareController(Resource):

    def get(self):
        return {"response" : "hello get"}

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
            x = args['x']
            y = args['y']
            nb = args['nb']
            species = args['species']

            square = Square(x, y, nb, species)
            db.session.add(square)
            db.session.commit()

            return {'x': args['x'], 'y': args['y'], nb: args['nb'], species: args['species']}

        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}

    def put(self):
        return {"response" : "hello put"}

    def delete(self):
        return {"response" : "hello delete"}
