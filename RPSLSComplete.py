# 'Devin Emerald/RockPaperScissorsLizardSpockProject/13August2022'
# '!/usr/bin/env python3'
# 'Importing Python's built-in module'
import random

# 'Global moves'
moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']


# 'Parent class for all players'
class Player:
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        pass


# 'Rock child class that plays only rock'
class Rock(Player):
    def move(self):
        return "rock"


# 'Random child class that plays random moves'
class Random(Player):
    def move(self):
        move = random.choice(moves)
        return (move)


# 'Human player that uses intergers as the input only'
class Human(Player):
    def __init__(self):
        Player.__init__(self)

    def move(self):
        while True:
            try:
                action = int(input("""0 = ROCK, 1 = PAPER, 2 = SCISSORS, \
3 = LIZARD, 4 = SPOCK \nSelect your interger/number: """))
                action = moves[action]
                print()
                return action
            except IndexError:
                print("Wrong number fool! Try again...")
                print()
            except ValueError:
                print("Wrong option fool! Try again...")
                print()


# 'Reflect child class where input of move1 is learned + transferred to move2
# as an output in the next round from None'
class Reflect(Player):
    def __init__(self):
        Player.__init__(self)
        self.their_move = None
        self.my_move = None

    def move(self):
        if self.their_move is None:
            return 'rock'
        else:
            self.their_move = self.my_move
        return self.my_move

    def learn(self, their_move, my_move):
        self.their_move = their_move
        self.my_move = my_move


# 'Cycle child class that cycles through moves from rock.'
class Cycle(Player):
    def __init__(self):
        Player.__init__(self)
        self.index_of_current_move = 0

    def move(self):
        next_move = moves[self.index_of_current_move]
        self.index_of_current_move = \
            (self.index_of_current_move + 1) % len(moves)
        return next_move
# 'Parent Game class'


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

# 'Function that plays one game, dsplays moves and scores
# also returns total score count to play_game'
    def play_round(self):
        p1_score = 0
        p2_score = 0
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if ((move1 == 'rock' and move2 == 'rock') or
            (move1 == 'paper' and move2 == 'paper') or
            (move1 == 'scissors' and move2 == 'scissors') or
            (move1 == 'lizard' and move2 == 'lizard') or
                (move1 == 'spock' and move2 == 'spock')):
            print()
            print(f"Players Draw! \n\nPlayer 1 used: {move1} \
\nPlayer 2 used: {move2}")
            print()
            print("Player 1 scored: "+str(p1_score) + "\
\nPlayer 2 scored: "+str(p2_score))
            print()
            print("---------------------------\
--------------------------------")
        elif ((move1 == 'paper' and move2 == 'spock') or
                (move1 == 'spock' and move2 == 'scissors') or
                (move1 == 'spock' and move2 == 'rock') or
                (move1 == 'rock' and move2 == 'lizard') or
                (move1 == 'scissors' and move2 == 'lizard') or
                (move1 == 'lizard' and move2 == 'paper') or
                (move1 == 'lizard' and move2 == 'spock') or
                (move1 == 'rock' and move2 == 'scissors') or
                (move1 == 'scissors' and move2 == 'paper') or
                (move1 == 'paper' and move2 == 'rock')):
            p1_score += 1
            print(f"Player 1 Wins! \n\nPlayer 1 used: {move1} \
\nPlayer 2 used: {move2}")
            print()
            print("Player 1 scored: "+str(p1_score) + "\
\nPlayer 2 scored: "+str(p2_score))
            print()
            print("----------------------------\
-------------------------------")
            return "P1"
        else:
            ((move2 == 'paper' and move1 == 'spock') or
                (move2 == 'spock' and move1 == 'scissors') or
                (move2 == 'spock' and move1 == 'rock') or
                (move2 == 'rock' and move1 == 'lizard') or
                (move2 == 'scissors' and move1 == 'lizard') or
                (move2 == 'lizard' and move1 == 'paper') or
                (move2 == 'lizard' and move1 == 'spock') or
                (move2 == 'rock' and move1 == 'scissors') or
                (move2 == 'paper' and move1 == 'rock'))
            p2_score += 1
            print(f"Player 2 Wins! \n\nPlayer 1 used: {move1} \
\nPlayer 2 used: {move2}")
            print()
            print("Player 1 scored: "+str(p1_score) + "\
\nPlayer 2 scored: "+str(p2_score))
            print()
            print("----------------------------\
-------------------------------")
            return "P2"

# 'Function that holds game statistics for total score'
    def play_game(self):
        p1_score = 0
        p2_score = 0
        print()
        print("Game start!")
        for round in range(1, 6):
            print()
            print(f"Round {round}:")
            winner = self.play_round()
            if winner == "P1":
                p1_score += 1
            elif winner == "P2":
                p2_score += 1
        print()
        print("Player 1 total score: "+str(p1_score))
        print("Player 2 total score: "+str(p2_score))
        print()
        print("""Game over!\
\n-----------------------------------------------------------""")


# 'Functions to call the game together'
if __name__ == '__main__':
    # 'Function to call on the character to play'
    strategies = {"1": Rock(), "2": Random(), "3": Reflect(), "4": Cycle()}
# 'Input function called first in the entire game to start'
    user_input = input("""Welcome to Dev's Rock, Paper,\
 Scissors, Lizard, Spock Game!
-----------------------------------------------------------
Rules of the game:
Rock beats Scissor and Lizard
Paper beats Rock and Spock
Scissor's beats Paper and Lizard
Lizard beats Paper and Spock
Spock beats Rock and Scissors
-----------------------------------------------------------
Each opponent has a different gameplay stategy!
Pick your opponent from the list available...
\nPress 1 for Rock!
Press 2 for Random!
Press 3 for Reflect!
Press 4 for Cycle!\n""")
# 'Second function to call, while loop for the character selection'
while True:
    try:
        game = Game(Human(), strategies[user_input])
    except KeyError:
        print("No KeyError here! Try the option only available fool!\n")
        user_input = input("""Press 1 for Rock!
Press 2 for Random!
Press 3 for Reflect!
Press 4 for Cycle!\n""")
    print()
    game_type = input("""Press 1 for a game or Press 2 for five rounds!\
 or Press 3 to QUIT!\
 Make your selection fool! \n""")
# 'This break is important, it helps for the program to
# not repeat and exit when the game has completed'
    break
# 'Third function to call to play the game as single or rounds or quit'
while True:
    try:
        if game_type == '1':
            option = game.play_round()
            input("Now you've seen the result, press Enter to leave fool!\n")
            break
        elif game_type == '2':
            option = game.play_game()
            input("Now you've seen the result, press Enter to leave fool!\n")
            break
        elif game_type == '3':
            quit
            break
        else:
            game_type = input("""Wrong fool!\
 Try it again properly, otherwise quit.\n""")
    except IndexError:
        print()
    except ValueError:
        print()
    except NameError:
        print()
        break
