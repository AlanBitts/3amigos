import random

class Card:
    '''
    Using a class to represent each card makes the deck more manageable and intuitive.
    The Card class can now handle cards without a suit, which is useful for jokers.
    '''
    def __init__(self, value, suit=None):
        self.value = value
        self.suit = suit

    def __repr__(self):
        if self.suit:
            return f"{self.value} of {self.suit}"
        else:
            return f"{self.value}"

def create_deck():
    '''
    Generates a list of Card objects, one for each combination of value and suit plus two joker cards.
    '''
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [Card(value, suit) for suit in suits for value in values]
    jokers = [Card('Joker'), Card('Joker')]
    deck.extend(jokers)
    return deck

def shuffle_deck(deck):
    '''
    Uses Python's built-in random.shuffle method to shuffle the deck in place
    '''
    random.shuffle(deck)

def deal_cards(deck, num_cards):
    '''
    Removes the specified number of cards from the deck and returns them as a list.
    '''
    return [deck.pop() for _ in range(num_cards)]

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.face_down = []
        self.face_up = []

    def receive_hand(self, cards):
        self.hand.extend(cards)

    def receive_face_down(self, cards):
        self.face_down.extend(cards)

    def receive_face_up(self, cards):
        self.face_up.extend(cards)

    def show_hand(self):
        return f"{self.name}'s hand: {self.hand}"

    def show_face_up(self):
        return f"{self.name}'s face-up cards: {self.face_up}"

    
    def draw_card(self, deck):
        '''
        allows players to draw a card from the deck.
        '''
        if deck:
            self.hand.append(deck.pop())
        else:
            print("No more cards in the deck!")

def create_players(names):
    '''
     generates a list of Player objects based on the provided names
    '''
    return [Player(name) for name in names]

def deal_to_players(deck, players):
    for player in players:
        player.receive_hand(deal_cards(deck, 3))
        player.receive_face_down(deal_cards(deck, 3))
        player.receive_face_up(deal_cards(deck, 3))
    return deck  # Return the remaining deck


def game_loop(players, deck):
    while deck:
        for player in players:
            print(f"\n{player.name}'s turn:")
            player.draw_card(deck)
            print(player.show_hand())
            if not deck:
                break

player_names = ['Alice', 'Bob', 'Charlie']
players = create_players(player_names)

# Create, shuffle the deck, and deal cards to each player
deck = create_deck()
shuffle_deck(deck)
remaining_deck = deal_to_players(deck, players)

# Show each player's hand and face-up cards
for player in players:
    print(player.show_hand())
    print(player.show_face_up())

# Show the remaining cards in the deck
#print("Remaining cards in the deck:", remaining_deck)

# Start the game loop
#game_loop(players, remaining_deck)