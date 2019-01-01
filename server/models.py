from api import db
import game.constants as constants


class Square(db.Model):

    class Species(db.Enum):
        vampire = 'VAMPIRE'
        werewolf = 'WEREWOLF'
        human = 'HUMAN'
        empty = 'EMPTY'

    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Integer, nullable=False, default=1)
    y = db.Column(db.Integer, nullable=False, default=1)
    nb = db.Column(db.Integer, nullable=True, default=0)
    species = db.Column(Species(name='species_values'), nullable=False, default=Species.empty)

    def __init__(self, x, y, nb, species):
        self.x = x
        self.y = y
        self.nb = nb
        self.species = species

    def __repr__(self):
        if self.species == constants.EMPTY:
            return 'Empty Square at position (x: {}, y: {})'.format(self.x, self.y)
        else:
            species = constants.MAP_SPECIES[int(self.species)]
            return '<{} {} at position (x: {}, y:{})>'.format(self.nb, species, self.x, self.y)


class PlayerTurn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    turn = db.Column(db.Boolean, nullable=False, default=True)

    def __init__(self, turn):
        self.turn = turn

    def __repr__(self):
        if self.turn:
            return '<{} turn>'.format(constants.MAP_SPECIES[int(constants.VAMPIRE)])
        else:
            return '<{} turn>'.format(constants.MAP_SPECIES[int(constants.WEREWOLF)])
