def get_surrounding_squares_with_species(attacked_square, attacking_species):
  from api import db
  from models import Square
  x, y = (attacked_square.x, attacked_square.y)
  return Square.query. \
                        filter(Square.x.in_((x, x + 1, x - 1))). \
                        filter(Square.y.in_((y, y + 1, y - 1))). \
                        filter(Square.species == attacking_species).all()


def check_if_authorized_movement(nb_attacking_species, attacking_species, attacked_square):
    list_surrounding_squares = get_surrounding_squares_with_species(attacked_square, attacking_species)
    total_nb_surrounding_species = 0
    for surrounding_square in list_surrounding_squares:
      total_nb_surrounding_species += surrounding_square.nb
    return int(nb_attacking_species) <= total_nb_surrounding_species
