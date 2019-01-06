from numpy.random import binomial
from game.constants import Species


class Game:
    attackingSpecies = Species.EMPTY
    attackedSpecies = Species.EMPTY
    nbAttackingSpecies = 0
    nbAttackedSpecies = 0
    fightResult = {}  # TODO: refactor into a class

    def __init__(self, attacking_species, attacked_species, nb_attacking_species, nb_attacked_species):
        self.attackingSpecies = attacking_species
        self.nbAttackingSpecies = int(nb_attacking_species)
        if attacked_species is not None:
            self.attackedSpecies = attacked_species
            self.nbAttackedSpecies = int(nb_attacked_species)

    def fightVsHuman(self):
        if self.nbAttackedSpecies < self.nbAttackingSpecies:
            self.fightResult['winningSpecies'] = str(self.attackingSpecies)
            self.fightResult['nbWinningSpecies'] = int(self.nbAttackingSpecies + self.nbAttackedSpecies)
            return self.fightResult
        else:
            winProbability = self.nbAttackingSpecies / (2 * self.nbAttackedSpecies)
            if binomial(1, winProbability) == 1:
                nbAttackingSpeciesSurvivors = 0
                nbHumanConverted = 0
                for i in range(self.nbAttackingSpecies):
                    nbAttackingSpeciesSurvivors += binomial(1, winProbability)
                for i in range(self.nbAttackedSpecies):
                    nbHumanConverted += binomial(1, winProbability)
                self.fightResult['winningSpecies'] = self.attackingSpecies
                self.fightResult['nbWinningSpecies'] = nbAttackingSpeciesSurvivors + nbHumanConverted
                return self.fightResult
            else:
                survivalProbability = 1 - (self.nbAttackingSpecies / (2 * self.nbAttackedSpecies))
                nbHumanSurvivors = 0
                for i in range(self.nbAttackedSpecies):
                    nbHumanSurvivors += binomial(1, survivalProbability)
                self.fightResult['winningSpecies'] = self.attackedSpecies
                self.fightResult['nbWinningSpecies'] = nbHumanSurvivors
                return self.fightResult

    def fightVsMonsters(self):
        if 1.5 * self.nbAttackedSpecies < self.nbAttackingSpecies:
            self.fightResult['winningSpecies'] = str(self.attackingSpecies)
            self.fightResult['nbWinningSpecies'] = int(self.nbAttackedSpecies + self.nbAttackedSpecies)
            return self.fightResult
        else:
            winProbability = self.nbAttackingSpecies / (2 * self.nbAttackedSpecies)
            if self.nbAttackingSpecies <= self.nbAttackedSpecies <= 1.5 * self.nbAttackingSpecies:
                winProbability = (self.nbAttackingSpecies / self.nbAttackedSpecies) - 0.5
            if binomial(1, winProbability) == 1:
                nbAttackingSpeciesSurvivors = 0
                for i in range(int(self.nbAttackingSpecies)):
                    nbAttackingSpeciesSurvivors += binomial(1, winProbability)
                if nbAttackingSpeciesSurvivors == 0:
                    self.fightResult['winningSpecies'] = Species.EMPTY
                    self.fightResult['nbWinningSpecies'] = 0
                    return self.fightResult
                self.fightResult['winningSpecies'] = str(self.attackingSpecies)
                self.fightResult['nbWinningSpecies'] = int(nbAttackingSpeciesSurvivors)
                return self.fightResult
            else:
                survivalProbability = 1 - (self.nbAttackingSpecies / (2 * self.nbAttackedSpecies))
                nbAttackedSpeciesSurvivors = 0
                for i in range(int(self.nbAttackedSpecies)):
                    nbAttackedSpeciesSurvivors += binomial(1, survivalProbability)
                if nbAttackedSpeciesSurvivors == 0:
                    self.fightResult['winningSpecies'] = Species.EMPTY
                    self.fightResult['nbWinningSpecies'] = 0
                    return self.fightResult
                self.fightResult['winningSpecies'] = str(self.attackedSpecies)
                self.fightResult['nbWinningSpecies'] = int(nbAttackedSpeciesSurvivors)
                return self.fightResult

    def fightOrMerge(self):
        return {
          'winningSpecies': self.attackingSpecies,
          'nbWinningSpecies': self.nbAttackingSpecies
        }
        # if self.attackedSpecies == self.attackingSpecies:
        #     self.fightResult['winningSpecies'] = str(self.attackingSpecies)
        #     self.fightResult['nbWinningSpecies'] = int(self.nbAttackingSpecies + self.nbAttackedSpecies)
        #     return self.fightResult
        # if self.attackedSpecies == Square.Species.EMPTY:
        #     self.fightResult['winningSpecies'] = str(self.attackingSpecies)
        #     self.fightResult['nbWinningSpecies'] = int(self.nbAttackingSpecies)
        #     return self.fightResult
        # elif self.attackedSpecies == Square.Species.HUMAN:
        #     return self.fightVsHuman()
        # else:
        #     return self.fightVsMonsters()
