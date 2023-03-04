import random

class Card:
    def __init__(self, rank, suit):
        # Initializes the card with its rank and suit
        # and assigns it a value based on its rank
        self.rank = rank
        self.suit = suit
        if rank in ['10', 'Jack', 'Queen', 'King']:
            self.value = 10
        elif rank == 'Ace':
            self.value = 11
        else:
            self.value = int(rank)

           
class Deck:


class Player:        


class Dealer:


class Game:


# main loop