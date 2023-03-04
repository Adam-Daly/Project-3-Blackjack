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

    # add a card to the player's hand
    def add_card(self, card):
        self.hand.append(card)

    # calculate the score of the player's hand, accounting for aces
    def get_score(self):
        score = sum(card.value for card in self.hand)
        if score > 21:
            for card in self.hand:
                if card.rank == 'Ace' and score > 21:
                    score -= 10
        return score

    # ask the player how much they want to bet
    # and keep asking until they enter a valid bet amount
    def bet(self):
        while True:
            try:
                self.bet_amount = int(input(f"You have {self.money} dollars. How much would you like to bet? \n"))
                if self.bet_amount > self.money:
                    print("You can't bet more than you have!")
                else:
                    self.money -= self.bet_amount
                    break
            except ValueError:
                print("Please enter a valid bet amount.")

    # ask the player what action they want to take (hit, stand, or double down)
    # and perform the appropriate action
    def turn(self):
        # Keep looping until the player chooses to stand or bust
        while True:
            # Print the player's hand and score
            print(f"Your hand: {[str(card) for card in self.hand]}")
            print(f"Your score: {self.get_score()}")
            # Ask the player what action they want to take
            action = input("Hit, Stand, or Double Down? \n").lower()
            # If the player chooses to hit, add a new card to their hand
            #  and check if they busted
            if action == "hit":
                self.add_card(game.deck.deal())
                score = self.get_score()
                if score > 21:
                    # If the player busted, end the turn
                    print(f"Bust! Your score is {score}")
                    break            
            # If the player chooses to stand, end the turn
            elif action == "stand":
                break
            # If the player chooses to double down, add a new card to their hand
            # and double their bet
            elif action == "double down":
                if self.money < self.bet_amount:
                    print("You don't have enough money to double down!")
                else:
                    # Double the player's bet
                    # and deduct the additional bet from their money
                    self.money -= self.bet_amount
                    self.bet_amount *= 2
                    # Add a new card to the player's hand
                    # and check if they busted
                    self.add_card(game.deck.deal())
                    score = self.get_score()
                    if score > 21:
                        print(f"Bust! Your score is {score}")
                        break
            else:
                print("Invalid action, please try again.")

    # reset the player's hand
    def reset_hand(self):
        self.hand = []


class Dealer:
    # Initialize an empty hand for the dealer
    def __init__(self):
        self.hand = []

    # Add a card to the dealer's hand
    def add_card(self, card):
        self.hand.append(card)

    # Calculate the score of the dealer's hand
    def get_score(self):
        score = sum(card.value for card in self.hand)
        # If the dealer has an ace and their score is over 21,
        # treat the ace as a 1 instead of 11
        if score > 21:
            for card in self.hand:
                if card.rank == 'Ace' and score > 21:
                    score -= 10
        return score

    # Dealer takes their turn
    def turn(self):
        # Dealer must hit if their score is less than 17
        while self.get_score() < 17:
            self.add_card(game.deck.deal())
        print(f"Dealer's hand: {[str(card) for card in self.hand]}")
        print(f"Dealer's score: {self.get_score()}")

    # Reset the dealer's hand
    def reset_hand(self):
        self.hand = []


class Game:
    # initialize the player, dealer, deck, wins, and losses
    def __init__(self):
        self.player = Player(starting_money)
        self.dealer = Dealer()
        self.deck = Deck()
        self.wins = 0
        self.losses = 0

# main loop