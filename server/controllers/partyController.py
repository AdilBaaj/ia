from flask_restful import Resource
from game.constants import Species


class PartyController(Resource):

    # Creates a new board
    def post(self):
        from api import db
        from models import Square, PlayerTurn

        try:
            db.session.query(Square).delete()

            # TODO : add table related to a board that holds the size
            board_height = 15
            board_width = 15

            for i in range(board_width):
                for j in range(board_height):
                    square = Square(i, j, None, Species.EMPTY)
                    db.session.add(square)

            # Add a square with vampires
            self.update_square(0, 0, 10, Species.VAMPIRE)

            # Add a square with werewolves
            self.update_square(14, 14, 10, Species.WEREWOLF)

            # Add a square with human
            self.update_square(7, 7, 10, Species.HUMAN)
            
            # Set player turn
            turn = db.session.query(PlayerTurn).first()
            turn =
            db.session.commit()
            return {'message': 'New board created'}
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}


    @staticmethod
    def update_square(x, y, nb, species):
        from models import Square
        square = Square.query.filter_by(x=x, y=y).first()
        square.species = species
        square.nb = nb
        return square
