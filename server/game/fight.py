import constants
from numpy.random import binomial

class Game:
    attackingSpecies = constants.EMPTY
    attackedSpecies = constants.EMPTY
    nbAttackingSpecies = 0
    nbAttackedSpecies = 0
    fightResult = {}

    def __init__(self, attackingSpecies, attackedSpecies, nbAttackingSpecies, nbAttackedSpecies):
        self.attackingSpecies = attackingSpecies
        self.attackedSpecies = attackedSpecies
        self.nbAttackingSpecies = nbAttackingSpecies
        self.nbAttackedSpecies = nbAttackedSpecies

    def fightVsHuman(self):
        if self.nbAttackedSpecies < self.nbAttackingSpecies:
            fightResult['winningSpecies'] = self.attackingSpecies
            fightResult['nbWinningSpecies'] = self.nbAttackedSpecies + self.nbAttackedSpecies
            return fightResult
        else:
            if binomial(1, winProbability) == 1:
                winProbability = self.nbAttackingSpecies / ( 2  * self.nbAttackedSpecies)
                nbAttackingSpeciesSurvivors = 0
                nbHumanConverted = 0
                for i in range(self.nbAttackingSpecies):
                    nbAttackingSpeciesSurvivors += binomial(1, winProbability)
                for i in range(self.nbAttackedSpecies):
                    nbHumanConverted += binomial(1, winProbability)
                fightResult['winningSpecies'] = self.attackingSpecies
                fightResult['nbWinningSpecies'] = nbAttackingSpeciesSurvivors + nbHumanConverted
                return fightResult
            else:
                survivalProbability = 1 - (self.nbAttackingSpecies / ( 2  * self.nbAttackedSpecies))
                nbHumanSurvivors = 0
                for i in range(self.nbAttackedSpecies):
                    nbHumanSurvivors += binomial(1, survivalProbability)
                fightResult['winningSpecies'] = self.attackedSpecies
                fightResult['nbWinningSpecies'] = nbHumanSurvivors
                return fightResult

    def fightVsMonsters(self):
        if self.nbAttackedSpecies < 1.5 * self.nbAttackingSpecies:
            fightResult['winningSpecies'] = self.attackingSpecies
            fightResult['nbWinningSpecies'] = self.nbAttackedSpecies + self.nbAttackedSpecies
            return fightResult
        else:
            winProbability = self.nbAttackingSpecies / ( 2  * self.nbAttackedSpecies)
            if 1.5 * self.nbAttackingSpecies <= self.nbAttackedSpecies <= self.nbAttackingSpecies:
                winProbability = (self.nbAttackingSpecies / self.nbAttackedSpecies) - 0.5
            if binomial(1, winProbability) == 1:
                nbAttackingSpeciesSurvivors = 0
                for i in range(self.nbAttackingSpecies):
                    nbAttackingSpeciesSurvivors += binomial(1, winProbability)
                fightResult['winningSpecies'] = self.attackingSpecies
                fightResult['nbWinningSpecies'] = nbAttackingSpeciesSurvivors
                return fightResult
            else:
                survivalProbability = 1 - (self.nbAttackingSpecies / ( 2  * self.nbAttackedSpecies))
                nbAttackedSpeciesSurvivors = 0
                for i in range(self.nbAttackedSpecies):
                    nbAttackedSpeciesSurvivors += binomial(1, survivalProbability)
                fightResult['winningSpecies'] = self.attackedSpecies
                fightResult['nbWinningSpecies'] = nbAttackedSpeciesSurvivors
                return fightResult

    def fight(self):
        if self.attackedSpecies == constants.EMPTY:
            self.fightResult['winningSpecies'] = self.attackingSpecies
            self.fightResult['nbWinningSpecies'] = self.nbAttackingSpecies
            return self.fightResult
        elif self.attackedSpecies == constants.HUMAN:
            return self.fightVsHuman()
        else:
            return self.fightVsMonsters()


class Grid:
    'Common base class for all employees'
    xGridSize = 15
    yGridSize = 15

    def __init__(self, xGridSize, yGridSize):
        print("Instantiating new grid")
        self.xGridSize = xGridSize
        self.yGridSize = yGridSize

class Square:

    def __init__(self,species,nb,x,y,case_id):
		self.species = species
		self.nb = nb
		self.x = x
		self.y = y
		self.index = int(str(x)+str(y))
    def __repr__(self):
        return str([self.species,self.nb,self.x,self.y,self.index])
