import game.constants as constants
from numpy.random import binomial


class Game:
    attackingSpecies = constants.EMPTY
    attackedSpecies = constants.EMPTY
    nbAttackingSpecies = 0
    nbAttackedSpecies = 0
    fightResult = {}

    def __init__(self, attackingSpecies, attackedSpecies, nbAttackingSpecies, nbAttackedSpecies):
        self.attackingSpecies = int(attackingSpecies)
        self.nbAttackingSpecies = float(nbAttackingSpecies)
        if attackedSpecies is not None:
            self.attackedSpecies = int(attackedSpecies)
            self.nbAttackedSpecies = float(nbAttackedSpecies)

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
                    self.fightResult['winningSpecies'] = constants.EMPTY
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
                    self.fightResult['winningSpecies'] = str(constants.EMPTY)
                    self.fightResult['nbWinningSpecies'] = 0
                    return self.fightResult
                self.fightResult['winningSpecies'] = str(self.attackedSpecies)
                self.fightResult['nbWinningSpecies'] = int(nbAttackedSpeciesSurvivors)
                return self.fightResult

    def fightOrMerge(self):
        if self.attackedSpecies == self.attackingSpecies:
            self.fightResult['winningSpecies'] = str(self.attackingSpecies)
            self.fightResult['nbWinningSpecies'] = int(self.nbAttackingSpecies + self.nbAttackedSpecies)
            return self.fightResult
        if self.attackedSpecies == constants.EMPTY:
            self.fightResult['winningSpecies'] = str(self.attackingSpecies)
            self.fightResult['nbWinningSpecies'] = int(self.nbAttackingSpecies)
            return self.fightResult
        elif self.attackedSpecies == constants.HUMAN:
            return self.fightVsHuman()
        else:
            return self.fightVsMonsters()
