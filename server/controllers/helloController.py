from flask_restful import Resource
from flask_restful import reqparse


class HelloController(Resource):

    def get(self):
        return {"response" : "hello get"}

    def post(self):
        from api import db
        from models import User
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str, help='Email')
            parser.add_argument('username', type=str, help='Username')
            args = parser.parse_args()
            email = args['email']
            username = args['username']

            user = User(email, username)
            db.session.add(user)
            db.session.commit()

            return {'Email': args['email'], 'Password': args['username']}

        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}
        print(self)

        return {"response" : "hello post"}

    def put(self):
        return {"response" : "hello put"}

    def delete(self):
        return {"response" : "hello delete"}
