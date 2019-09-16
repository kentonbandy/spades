from colorama import init, Fore, Back
init()

class GraphicalCard:
    long_value_to_short_value_dict = {"Jack": "J", "Queen": "Q", "King": "K", "Ace": "A"}
    # suit_to_symbol_dict = {"Clubs": Fore.WHITE + "♣" + Fore.RESET, "Diamonds": Fore.RED + "♦" + Fore.RESET, "Hearts": Fore.RED + "♥" + Fore.RESET, "Spades": Fore.WHITE + "♠" + Fore.RESET}
    suit_to_symbol_dict = {"Clubs": "♣", "Diamonds": "♦", "Hearts": "♥", "Spades": "♠"}
    color_dict = {"Clubs": Fore.WHITE, "Diamonds": Fore.RED, "Hearts": Fore.RED, "Spades": Fore.WHITE}

    def __init__(self, card_name):
        self.card_name = card_name
        split = card_name.split(" ")
        self.value = self.card_to_short_value(split[0])
        self.suit = self.card_to_suit_symbol(split[-1])
        self.color = self.color_dict[split[-1]]

    def card_to_short_value(self, value):
        return self.long_value_to_short_value_dict.get(value, value).ljust(2)

    def card_to_suit_symbol(self, suit):
        return self.suit_to_symbol_dict[suit]

    def line_1(self):
        print("╭──── ", end="")

    def line_2(self):
        print(f"│ {self.color}{self.value}{Fore.RESET} ", end=" ")

    def line_3(self):
        print(f"│ {self.color}{self.suit}{Fore.RESET}  ", end=" ")

def graphical_hand(hand):
    graphical_cards = [GraphicalCard(card) for card in hand]
    for card in graphical_cards:
        card.line_1()
    print()

    for card in graphical_cards:
        card.line_2()
    print()

    for card in graphical_cards:
        card.line_3()
    print()
