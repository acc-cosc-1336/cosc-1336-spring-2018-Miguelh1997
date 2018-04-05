#write import statement for Die class
from src.homework.die import Die

'''
Create a Player class.

'''


class Player:

    def __init__(self):
        self.die = Die()
        self.die1 = self.die.roll()
        self.die2 = self.die.roll()

        '''
        Constructor method creates two Die attributes die1 and die2
        '''

    def roll_doubles(self):
        while self.die1 != self.die2:
            print(' Die 1:', self.die1, ' Die 2: ', self.die2)
            self.die1 = self.die.roll()
            self.die2 = self.die.roll()
        print('You got a double: ', self.die1)










