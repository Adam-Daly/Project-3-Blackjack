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

    def __str__(self):
        # Returns a string representation of the card
        return f"{self.rank} of {self.suit}"
           
class Deck:
    # Initializes the deck with 52 cards, each having a rank and suit
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = []
        # Initialize the deck of cards by iterating over each possible
        # combination of rank and suit and creating a new Card object for
        # each combination, which is then added to the self.cards list.
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        # Shuffles the deck in a random order
        random.shuffle(self.cards)

    def deal(self):
        # Removes and returns the top card from the deck
        return self.cards.pop()


class Player:        
    # initialize the hand, money, and bet_amount
    def __init__(self, starting_money):
        self.hand = []
        self.money = starting_money
        self.bet_amount = 0

class Dealer:


class Game:


# main loop