import random

# Class
class Main:
    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] # The Cards that can be added to a deck
        self.card = 0   # The Card that will be added to a deck
        self.player_deck = [] # Player's deck
        self.dealer_deck = [] # Dealer's deck
        self.player_total = 0
        self.dealer_total = 0
 
    # Function that shuffles the cards
    def deck(self):
        self.card = random.choice(self.cards) # Chooses a random card
        return self.card

    # Function for the Player's deck
    def player(self):
        self.deck() # Calls the deck function
        self.player_deck.append(self.card) # Adds a random card to the Player's deck
        self.player_score()
        # print(self.player_deck)
        return self.player_deck

    # Function for the Dealer's deck
    def dealer(self):
        self.deck() # Calls the deck function
        self.dealer_deck.append(self.card) # Adds a random card to the Dealer's deck
        self.dealer_score()
        # print(self.dealer_deck)
        return self.dealer_deck

    # Function for the Player's score
    def player_score(self):
        self.player_total = sum(self.player_deck) # Adds up all the cards for a score
        # print(self.player_total)
        return self.player_total

    # Function for the Dealer's score
    def dealer_score(self):
        self.dealer_total = sum(self.dealer_deck) # Adds up all the cards for a score
        # print(self.dealer_total)
        return self.dealer_total

    # Start of game
    def game(self):
        self.player()
        self.player()
        self.dealer()
        self.dealer()
        player_input = ""
        print(f"\nYour cards {self.player_deck}")
        print("\n##########################\n")
        while self.player_total < 21: # This loops until player score reachs 21 or over
            print(f"Player's Deck: {self.player_deck}")
            print(f"Score: {self.player_total}")
            player_input = input("hit or stand? > ")
            print("\n##########################\n")
            if player_input == "hit":
                self.player()
            else:
                print(f"Dealer's Deck: {self.dealer_deck}")
                print(f"Score: {self.dealer_total}")
                dealer_enter = input("Press Enter > ")
                print("\n##########################\n")
                for i in range(1, 3): # This loops until dealer reaches 1-3
                    self.dealer()
                    print(f"Dealer's Deck: {self.dealer_deck}")
                    print(f"Score: {self.dealer_total}")
                    dealer_enter = input(" Press Enter > ")
                    print("\n##########################\n")
                    if self.dealer_total == 21:
                        print(self.dealer_deck)
                        print(f"Score: {self.dealer_total}\n")
                        print("Dealer got Blackjack\n")
                        exit(x.game)
                    elif self.dealer_total > 21:
                        print(self.dealer_deck)
                        print(f"Score: {self.dealer_total}\n")
                        print("Dealer busted!\n")
                        exit(x.game)
                if self.dealer_total > self.player_total:
                    print(f"Player's Deck: {self.player_deck}")
                    print(f"Score: {self.player_total}\n")
                    print(f"Dealer's Deck: {self.dealer_deck}")
                    print(f"Score: {self.dealer_total}\n")
                    print("Dealer wins!\n")
                    exit(x.game)
                elif self.dealer_total < self.player_total:
                    print(f"Player's Deck: {self.player_deck}")
                    print(f"Score: {self.player_total}\n")
                    print(f"Dealer's Deck: {self.dealer_deck}")
                    print(f"Score: {self.dealer_total}\n")
                    print("Player wins!\n")
                    exit(x.game)
                else:
                    print("Error\n")
                    exit(x.game)
        if self.player_total == 21:
            print(f"Player's Deck: {self.player_deck}")
            print(f"Score: {self.player_total}\n")
            print("Player got Blackjack!\n")
        elif self.player_total > 21:
            print(f"Player's Deck: {self.player_deck}")
            print(f"Score: {self.player_total}\n")
            print("Player busted!\n")
        else:
            print("Error\n")

x = Main()
x.game()
