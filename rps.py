#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    # set the number of players
    def __init__(self):
        self.firstplayer = None
        self.secondplayer = None

    def learn(self, my_move, their_move):
        self.firstplayer = my_move
        self.secondplayer = their_move


class random_player(Player):
    def move(self):
        # computer make a random move
        return random.choice(moves)


class repeat_player(Player):
    def move(self):
        return "rock"


class human_player(Player):
    # Make a move
    def move(self):
        options = input("Choose your move\n"
                        "rock, paper, scissors\n").lower()

        if options in moves:
            return options
        else:
            print("You chose a wrong move\n")
            return self.move()


class opponent_player(Player):
    def move(self):
        # human opponent make a move
        human_move = input("Second Player\n"
                           "make a move:\n").lower()
        if human_move in moves:
            return human_move
        else:
            print("Wrong move, select a move from the options")
            return self.move()


class reflect_player(Player):
    def move(self):
        if self.secondplayer is None:
            return random.choice(moves)
        else:
            return self.secondplayer


class cycle_player(Player):
    def move(self):
        if self.firstplayer == moves[0]:
            return moves[1]
        elif self.firstplayer == moves[1]:
            return moves[2]
        else:
            return moves[0]


class Game:
    # set the gameplay and scores
    def __init__(self, playerone, playertwo):
        self.my_move = playerone
        self.their_move = playertwo

        self.p1 = 0
        self.their_move.score = 0

    def Game_play(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        move1 = self.my_move.move()
        move2 = self.their_move.move()

        print(f"Player 1: {move1}  Player 2: {move2}")

        if self.Game_play(move1, move2):

            self.p1 += 1
            print("Player One wins")
            print(f"Player One: {self.p1}\n"
                  f"Player Two: {self.their_move.score}\n")

        elif move1 == move2:
            print("Its a Tie")
            self.p1 += int("0")
            self.their_move.score += int("0")

            print(f"Player One: {self.p1}\n"
                  f"Player Two: {self.their_move.score}\n")

        else:
            print("Player Two wins")
            self.their_move.score += 1
            print(f"Player One: {self.p1}\n"
                  f"Player Two: {self.their_move.score}\n")

        self.my_move.learn(move1, move2)
        self.their_move.learn(move2, move1)

    def play_game(self):
        # set the start of the game and the number of rounds

        self.p1 = 0
        self.their_move.score = 0

        print("Game start!")
        for round in range(3):
            print(f"Round {round}:\n")
            self.play_round()
        print("Game over!\n")
        self.result()

    def result(self):
        # set the final score and the winner of the game
        print("Final Score\n"
              f"Player One {self.p1}\n"
              f"PLayer Two {self.their_move.score}\n")

        if self.p1 > self.their_move.score:
            print("The winner is Player One\n\n")
        elif self.their_move.score > self.p1:
            print("The winner is Player Two\n\n")
        else:
            print("Its a Tie\n\n")

        self.play_again()

    def play_again(self):
        choice = input("Do you wish to play again\n"
                       "yes or No\n").lower()
        if 'yes' in choice:
            game.play_game()
        else:
            print("Thanks for playing, goodbye!!!")
        exit()


if __name__ == '__main__':

    moves = ['rock', 'paper', 'scissors']

    while True:
        print("Rock, Paper, Scissors Game\n")
        print("Rules of the Game: Rock destorys Scissors\n"
              "                   Scissors cut Paper\n"
              "                   Paper covers Rock\n")

        game = Game(human_player(),
                    random.choice([opponent_player(),
                                   repeat_player(),
                                   reflect_player(),
                                   cycle_player(),
                                   random_player()]))
        game.play_game()
