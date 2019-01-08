from game.constants import Species
from api import db


class Square(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Integer, nullable=False, default=1)
    y = db.Column(db.Integer, nullable=False, default=1)
    nb = db.Column(db.Integer, nullable=True, default=0)
    species = db.Column(db.String, nullable=False, default=Species.EMPTY)

    def __init__(self, x, y, nb, species):
        self.x = x
        self.y = y
        self.nb = nb
        self.species = species

    def __repr__(self):
        if self.species == self.Species.EMPTY:
            return 'Empty Square at position (x: {}, y: {})'.format(self.x, self.y)
        else:
            return '<{} {} at position (x: {}, y:{})>'.format(self.nb, self.species, self.x, self.y)


class PlayerTurn(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    turn = db.Column(db.String, nullable=False, default=Species.VAMPIRE)

    def __init__(self, turn):
        self.turn = turn

    def __repr__(self):
        if self.turn:
            return '<{} turn>'.format(Species.VAMPIRE)
        else:
            return '<{} turn>'.format(Species.WEREWOLF)
