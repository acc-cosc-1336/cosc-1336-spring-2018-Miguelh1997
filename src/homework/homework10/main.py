from player import Player

from game_log import GameLog



#Create a game log instance

g = GameLog()

#SEnd the game_log instance to Player class as an argument
Player(g).roll_doubles()


#call the game log display method below
GameLog().display_log()




