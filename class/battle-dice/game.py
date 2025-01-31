import random
from character import Character

class Game:
    ''' Manages the Dice Battle game logic. '''

    def __init__(self, player1: Character, player2: Character):
        ''' Initializes the game with 2 players. '''
        self.__player1 = player1
        self.__player2 = player2


    def attack(self, attacker: Character, defender: Character):
        ''' Performs an attack where the attacker rolls a die to determine damage dealt. '''
        roll = random.randint(1, 6)
        dmg = roll * attacker.attack_power
        print(f"{attacker.name} rolled a {roll} and dealt {dmg} damage!")
        defender.health -= dmg
        print(f"{self.__player1.name}'s health: {self.__player1.health}       {self.__player2.name}'s health: {self.__player2.health}")

    def start_battle(self):
        ''' Starts a turn-based battle between two players. '''
        while self.__player1.health > 0 and self.__player2.health > 0:
            self.attack(self.__player1, self.__player2)
            if self.__player1.health > 0 and self.__player2.health > 0:
                self.attack(self.__player2, self.__player1)
        if self.__player1.health <= 0:
            print(f"{self.__player2.name} wins! Final health: {self.__player2.health}")
        else:
            print(f"{self.__player1.name} wins! Final health: {self.__player1.health}")
