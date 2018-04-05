import random
'''
Create a Die class to model a game day with 6 sides and values 1,2,3,4,5, and 6.

'''


class Die:

    def __init__(self):
        self.sides = 6
        '''
        Define a constructor method with one attribute sides with a values of 6.
        '''

    def roll(self):
        return random.randint(1, self.sides)














