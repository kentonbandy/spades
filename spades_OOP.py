import random
from spades import shuffle_deck, sort_hand, clear, wait
from graphical_card import graphical_hand

"""
1. main menu
2. deal cards
3. ask for blind bid
4. show hand
5. ask for bid (if not blind)
6. begin round
7. score round
8. if no score over 300: go to 2 else: declare winner
9. go to 1

classes:
player
"""


class Player:
    def __init__(self, name, score=0, blind=False, hand=[], bid=None):
        self.name = name
        self.score = score
        self.blind = blind
        self.hand = hand
        self.bid = bid
    
    def clear_score():
        self.score = 0

    def add_to_score(num):
        self.score += num


class Card:
    def __init__(self, name, score):
        self.short = name
        self.score = score
        self.get_long(name)
    
    def get_long(self, short):
        """creates full name of card as well as setting val and suit"""
        key = {
            "j": "Jack",
            "q": "Queen",
            "k": "King",
            "a": "Ace",
            "h": "Hearts",
            "c": "Clubs",
            "d": "Diamonds",
            "s": "Spades"
        }
        v = short[0]
        if v in key.keys():
            self.val = key[v]
        elif v == "1":
            self.val = 10
        else:
            self.val = int(v)
        self.suit = key[short[-1]]
        self.name = str(self.val) + " of " + self.suit


def build_deck():
    """builds a deck composed of Card objects"""
    deck = []
    suits = ["h", "c", "d", "s"]
    faces = ["j", "q", "k", "a"]
    for suit in suits:
        for n in range(2, 11):
            deck.append(str(n) + suit)
        for f in faces:
            deck.append(f + suit)
    i = 0
    deck = [Card(card, deck.index(card) % 13) for card in deck]
    for card in deck:
        if card.suit == "Spades":
            card.score += 13
    return deck


def init_order(players):
    """chooses a starting player at random by rotating the player list"""
    """players are always 'seated' with the same orientation"""
    rnum = random.randint(0, 3)
    new_order = []
    new_order.extend(players[rnum:])
    new_order.extend(players[:rnum])
    return new_order


you = Player("You")
yasmine = Player("Yasmine")
florian = Player("Florian")
sakura = Player("Sakura")
players = init_order([you, yasmine, florian, sakura])
high_score = 0


def deal_cards():
    deck = build_deck()
    shuffled_deck = shuffle_deck(deck)
    low_ind = 0
    high_ind = 13
    for player in players:
        player.hand = sort_hand(shuffled_deck[low_ind:high_ind], deck)
        low_ind += 13
        high_ind += 13


def blind_bid():
    while True:
        clear()
        inp = (input("Would you like to bid on the blind? y/n:\n")).lower()
        if inp == "y":
            you.blind = True
            return True
        elif inp == "n":
            you.blind = False
            return False
        else:
            print("Please answer with a \"y\" or \"n\".")
            wait(2)


def bidding():
    if not blind_bid():
        graphical_hand(you.hand)
    




deal_cards()
for card in you.hand:
    print(card.name)
    print(card.score)
    print(card.val)
    print(card.suit)
    print(card.short)


"""
if __name__ == "__main__":
    main_menu()
    while high_score < 300:
        deal_cards()
        bidding()
        play_round()
        display_score()
        high_score = get_high_score()

"""