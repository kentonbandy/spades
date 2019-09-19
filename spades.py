
import time
import random
import platform
import subprocess
import sys
import os
import textwrap

from graphical_card import graphical_hand

"""TO DO:
make moar dictionaries
update scoring to account for nil bidding
implement sleep
make bot bids smarter (more realistic - they're bidding a little too high)
make bot trick play smarter (look at played cards)
general cleanup
make error messages less annoying
(maybe display the message at the bottom and then refresh)
"""

import signal


def signal_handler(sig, frame):
        print('\nGoodbye!')
        quit()
signal.signal(signal.SIGINT, signal_handler)


def wait(seconds=0.3):
    return
    # time.sleep(seconds)


def clear():
    """Clears the terminal screen."""
    if platform.system().lower() == "windows":
        os.system('cls')
    else:
        sys.stdout.write('\033[2J\033[1;1H')


rectangle = """
-------------------------------------------------------------------------------
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                Resize your window so that the edges of                      |
|                this rectangle are visible and not                           |
|                distorted for the best playing experience!                   |
|                                                                             |
|                                                                             |
|                Press enter when you are done.                               |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
------------------------------------------------------------------------------
"""


def main_menu():
    while True:
        clear()
        print("                 /\\")
        print("               /    \\")
        print("             /        \\")
        print("            |          |")
        print("             `..``.``..`")
        print("                 .:.")
        print("\n                SPADES")
        print("         " + version)
        print("            By Kenton Bandy")
        print("                 2019")
        print("\nPlay a game of spades with your friends")
        print("    Yasmine, Florian, and Sakura.\n")
        print("Main Menu:")
        print("\n1. Begin Game")
        print("2. How to Play (recommended for first time players)")
        print("3. Calibrate Window Size")
        print("4. Acknowledgements")
        print("5. End Game")
        prompt = input(
            "\nWhat would you like to do? Enter the number of your choice:\n")
        if prompt == "1":
            break
        elif prompt == "2":
            clear()
            print("How to Play:\n")
            print(
                "You will need to enter text inputs to play this", end="")
            print(" game. All you need to")
            print("do is follow the prompts to enter either the", end="")
            print(" number of your bid or the")
            print("card you want to play and press enter.")
            print()
            print("In this game, you can use shorthand to type your card:")
            print("Ace of Spades = \"as\", 10 of Hearts = \"10h\", etc.")
            print("You can also type out the full name of the card", end="")
            print(" if you wish.")
            print()
            print("For the rules of Spades, just search Google", end="")
            print(" for \"spades wikipedia\".")
            print("In this variant, the first to 300 points wins the", end="")
            print(" round. Sandbagging")
            print("occurs when a player has 5 or more points in the", end="")
            print(" ones place of their")
            print("total score, resulting in a loss of 55 points.", end="")
            print(" Players who exactly")
            print("match their blind bid win 100 extra points, with a", end="")
            print(" 100 point penalty")
            print("if they do not meet their blind bid.")
            print()
            print("Type \"q\" and press Enter to quit at any time.")
            practice()
            continue
        elif prompt == "3":
            clear()
            print(rectangle)
            input()
            continue
        elif prompt == "4":
            clear()
            print("              Acknowledgements:")
            print()
            print("Special thanks go to Travis and Brian for", end="")
            print(" being very generous ")
            print("with their help, suggestions, code review, and positivity.")
            print()
            print("Thanks to Brian (again) for creating the card graphics and")
            print("contributing to the code.")
            print("")
            print("Thanks to everyone who helped me develop this game", end="")
            print(" by play\ntesting it and offering feedback.")
            print("")
            print("Thank you, user, for playing the game!")
            press_enter()
        elif (
            prompt == "5" or prompt.lower() == "quit" or prompt.lower() == "q"
                ):
            clear()
            print("Thanks for playing!\n\n\n\n\n")
            quit()
        else:
            print("\nPlease enter the number of your choice (1, 2, or 3).")
            time.sleep(2)
            continue


def practice():
    while True:
        practice = input(
            "\nLet's practice! Try playing the Jack of Diamonds.\n")
        if practice.lower() == "jd" or practice.lower() == "jack of diamonds":
            print("\nWell done! Now you're ready to play.")
            time.sleep(2)
            break
        elif practice.lower() == "quit" or practice.lower() == "q":
            clear()
            print("Thanks for playing!\n\n\n\n\n")
            quit()
        else:
            print("\nThat didn't work! Try again, being careful", end="")
            print(" to type the card or shorthand correctly.")
            wait()
            continue


def press_enter():
    input("\nPress enter when you are ready to continue.")


def build_deck():
    """Creates and returns a standard deck of cards in an ordered list"""
    card_values = list(range(2, 11))
    card_values.extend(["Jack", "Queen", "King", "Ace"])
    suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
    deck = []
    for suit in suits:
        for value in card_values:
            deck.append(f"{value} of {suit}")
    return deck


def build_score_deck():
    """Creates and returns a standard deck of cards in order of strength"""
    card_values = list(range(2, 11))
    card_values.extend(["Jack", "Queen", "King", "Ace"])
    suits = ["Clubs", "Diamonds", "Hearts"]
    score_deck = []
    for value in card_values:
        for suit in suits:
            score_deck.append(f"{value} of {suit}")
    for value in card_values:
        score_deck.append(f"{value} of Spades")
    return score_deck


def build_shorthand(deck):
    shorthand_list = []
    for card in deck:
        n = card.split()
        val = n[0]
        suit = n[2]
        if val == "10":
            shorthand_list.append(f"{val}{suit[0]}".lower())
        else:
            shorthand_list.append(f"{val[0]}{suit[0]}".lower())
    return shorthand_list


def build_shorthand_dict(sh_list, deck):
    sh_dict = {}
    for i in range(52):
        sh_dict[sh_list[i]] = deck[i]
    return sh_dict


def shuffle_deck(deck):
    """Returns a shuffled deck made up of cards from the given deck"""
    print("\nShuffling the deck!")
    shuffled_deck = deck[:]
    random.shuffle(shuffled_deck)
    return(shuffled_deck)


def deal_cards(shuffled_deck):
    """Returns a hand of 13 cards each to four players from a shuffled deck"""
    hands = [[], [], [], []]
    print("Dealing the cards!")
    hands[0] = shuffled_deck[:13]
    hands[1] = shuffled_deck[13:26]
    hands[2] = shuffled_deck[26:39]
    hands[3] = shuffled_deck[39:]
    return hands


def sort_hand(hand, deck):
    """Returns a hand of cards sorted in the index order of the given deck"""
    sorted_hand = []
    for index in deck:
        for card in hand:
            if index == card:
                sorted_hand.append(card)
    return sorted_hand


def get_bid(hand, player_bids, play_order, blind):
    """Returns the user's bid"""
    while True:
        error = "\nPlease give a number from 0 to 13!\n"
        while True:
            blind_bid = input("Do you wish to bid on the blind? (y/n):\n")
            if blind_bid.lower() == "y" or blind_bid.lower() == "yes":
                blind["You"] = True
                break
            elif blind_bid.lower() == "n" or blind_bid.lower() == "no":
                blind["You"] = False
                break
            elif blind_bid.lower() == "q" or blind_bid.lower() -- "quit":
                clear()
                print("Thanks for playing!\n\n\n\n\n")
                quit()
            else:
                print("Please answer with a \"y\" or \"n\".")
                press_enter()
                clear()
                display_bids(player_bids, play_order)
                continue
        message = "Your turn to bid! (guess how many tricks"
        message += " you will win, 0-13)\n"
        if blind["You"] is True:
            bid = input(message)
        else:
            print("Your hand:")
            graphical_hand(hand)
            bid = input(message)
        if bid.lower() == "quit" or bid.lower() == "q":
            clear()
            print("Thanks for playing!\n\n\n\n\n")
            quit()
        try:
            num = int(bid)
        except ValueError:
            print(error)
            time.sleep(1)

            continue
        if (num >= 0) and (num <= 13):
            return num, blind
        else:
            print(error)
            time.sleep(1)
            continue


def bot_bid(bot_hand):
    """Returns a bid for one of the bots"""
    score = 0
    for card in bot_hand:
        if ("Ace" in card) or ("King" in card):
            score += 3
        if "Spades" in card:
            score += 0.25
        if ("Queen" in card) or ("Jack" in card):
            score += 2
    return int(score / 3) + 1


def get_order(round, players, offset):
    """Returns an order of players."""
    new_order = []
    new_order.extend(players[offset + round - 1:])
    new_order.extend(players[:offset + round - 1])
    return new_order


def display_bids(player_bids, play_order):
    clear()
    print("Let's place some bids! How many books will you win this round?\n")
    if play_order[0] == "You":
        print("You go first!\n")
    else:
        print(f"{play_order[0]} goes first!\n")
    for player in play_order:
        ind = players.index(player)
        if player_bids[ind] > -1:
            print(f"{players[ind].rjust(7)} bid {player_bids[ind]} tricks.")


def find_suit(card):
    """Returns the suit of the given card as a string"""
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    for suit in suits:
        if suit in card:
            return suit


def remove_spades(hand):
    """Returns a hand with the Spades removed."""
    spadeless_hand = hand[:]
    for card in hand:
        if "Spades" in card:
            spadeless_hand.remove(card)
    return spadeless_hand


def trick_score_deck(deck, suit):
    """Returns a list of cards in score order with irrelevant suits removed."""
    if suit == "Spades":
        return [card for card in deck if find_suit(card) == suit]
    else:
        ts_deck = [card for card in deck if find_suit(card) == suit]
        ts_deck.extend([card for card in deck if find_suit(card) == "Spades"])
        return ts_deck


def play_spade(user_card, hand, trick_pool, spaded, first_card):
    """Returns True if the card is a non-playable Spade"""
    hand_suits = [find_suit(card) for card in hand]
    if "Spades" not in user_card:
        return None
    elif (
        first_card and (
            "Spades" not in first_card) and (
                find_suit(first_card) in hand_suits)):
        clear()
        print("\nYou cannot play a Spade if you can play the", end="")
        print(" suit of the opening card.")
        print("Try playing a card in the same suit as the opening card.")
        return True
    elif (first_card == "") and (spaded is False):
        for suit in hand_suits:
            if suit != "Spades":
                clear()
                print("You cannot open with a Spade if you have", end="")
                print(" non-Spade cards and Spades have not been broken.")
                print("Try a non-spade card in your hand.")
                return True
    else:
        return None


def bot_play_card(hand, trick_pool, bid, tricks, spaded, first_card):
    """Returns a card from the current bot's hand"""
    score_deck = build_score_deck()
    spadeless_hand = sort_hand(remove_spades(hand), score_deck)
    scored_hand = sort_hand(hand, score_deck)
    hand_suits = [find_suit(card) for card in hand]
    first_suit = find_suit(first_card)
    if not first_card:
        if spaded is False:
            if spadeless_hand:
                if tricks < bid:
                    return spadeless_hand[-1]
                else:
                    return spadeless_hand[0]
            else:
                if tricks < bid:
                    return scored_hand[-1]
                else:
                    return scored_hand[0]
        else:
            if tricks < bid:
                return scored_hand[-1]
            else:
                return scored_hand[0]
    else:
        if first_suit in hand_suits:
            suited_hand = [
                card for card in scored_hand if find_suit(card) == first_suit]
            if tricks < bid:
                return suited_hand[-1]
            else:
                return suited_hand[0]
        elif spaded is True:
            if tricks < bid:
                return scored_hand[-1]
            else:
                return scored_hand[0]
        else:
            if spadeless_hand:
                if tricks < bid:
                    return spadeless_hand[-1]
                else:
                    return spadeless_hand[0]
            else:
                return scored_hand[0]


def card_formatter(card):
    if card.lower() == "quit" or card.lower() == "q":
        clear()
        print("Thanks for playing!\n\n\n\n\n")
        quit()
    elif card in sh_list:
        formatted_card = sh_dict[card]
        return formatted_card
    elif card.lower() in [i.lower() for i in main_deck]:
        card_lst = card.split()
        n = card_lst[0]
        s = card_lst[2]
        formatted_card = f"{n.title()} of {s.title()}"
        return formatted_card
    else:
        return None


def user_play_card(hand, trick_pool, play_order, spaded, first_card):
    """Prompts the user to play a card"""
    first_card_suit = find_suit(first_card)
    hand_suits = [find_suit(card) for card in hand]

    if first_card:
        print("\nYour hand:")
        graphical_hand(hand, find_suit(first_card))
        user_card = card_formatter(input(
            "\nWhich card would you like to play?\n"))
    else:
        print("\nYour hand:")
        graphical_hand(hand)
        user_card = card_formatter(input(
            "\nYou start the trick! Which card would you like to play?\n"))
    if user_card not in hand:
            clear()
            print("\nPlease choose a card in your hand!")
            print("Be sure to type it exactly as it appears in your hand,")
            print("or use the following shorthand: \"Ace of Spades\" = \"as\"")
            press_enter()
            return ""
    elif play_spade(user_card, hand, trick_pool, spaded, first_card):
        press_enter()
        return ""
    elif first_card_suit != find_suit(user_card):
        if first_card_suit in hand_suits:
            print("You have to play the same suit as the", end="")
            print(" opening card if possible.")
            press_enter()
            return ""
    return user_card


def determine_winner(trick_pool, tricks_won, first_card):
    ts_deck = trick_score_deck(build_score_deck(), find_suit(first_card))
    score = [0, 0, 0, 0]
    largest_score = -1000000000
    for card in trick_pool:
        for c in ts_deck:
            if card == c:
                score[trick_pool.index(card)] = ts_deck.index(c)
    for num in score:
        if num > largest_score:
            largest_score = num
            winner = score.index(num)
    tricks_won[winner] += 1
    print(f"\n{players[winner]} won the trick!")
    wait()
    print("\n...")
    return tricks_won, winner


def display_tricks_won(tricks_won, player_bids):
    for n in range(4):
        if players[n] == "You":
            hav = "have"
            nee = "need"
        else:
            hav = "has"
            nee = "needs"
        if tricks_won[n] == 1:
            tri = "trick"
        else:
            tri = "tricks"
        print(f"{players[n].rjust(7)} {hav} won {tricks_won[n]} {tri}", end="")
        print(f" and {nee} {player_bids[n]}.")
        wait(0.1)
    print()


def display_current_trick(trick_pool, player_hands, play_order):
    print(f"Trick {14 - len(player_hands[0])}/13:\n")

    for card in trick_pool:
        if players[trick_pool.index(card)] == play_order[0]:
            action = "opened with"
        else:
            action = "played"
        if card:
            ind = trick_pool.index(card)
            print(f"{players[ind]} {action} the {trick_pool[ind]}.")
    print()

    if players[trick_pool.index(card)] != play_order[0]:
        print("\nTrick pool:")
    play_order_pool = []
    for player in play_order:
        if trick_pool[players.index(player)]:
            play_order_pool.append(trick_pool[players.index(player)])
    if len(play_order_pool) > 0:
        graphical_hand(play_order_pool)


def get_scores(score, tricks, bids, blind):
    round_scores = [0, 0, 0, 0]
    high_scorers = []
    for i in range(4):
        key = players[i]
        base_num = bids[i] * 10
        if tricks[i] >= bids[i]:
            round_scores[i] += base_num + tricks[i] - bids[i]
        else:
            round_scores[i] -= base_num
            if players[i] == "You":
                print(f"You have set! Minus {base_num}!")
                wait()
            else:
                print(f"{players[i]} has set! Minus {base_num}!")
                wait()
        if blind[key] is True:
            if tricks[i] == bids[i]:
                round_scores[i] += 100
                if key == "You":
                    print("You met your blind bid! Plus 100!")
                else:
                    print(f"{key} met their blind bid! Plus 100!")
            elif tricks[i] < bids[i]:
                round_scores[i] -= 100
                if key == "You":
                    print("You didn't meet your blind bid! Minus 100!")
                else:
                    print(f"{key} didn't meet their blind bid! Minus 100!")
        score[key] += round_scores[i]
        if score[key] % 10 >= 5:
            score[key] -= 55
            round_scores[i] -= 55
            if key == "You":
                print(f"You have sandbagged! Minus 55!")
                wait()
            else:
                print(f"{key} has sandbagged! Minus 55!")
                wait()
    print("\nThis round's scores are as follows:")
    wait()
    for n in range(4):
        print(f"{players[n]} scored {round_scores[n]} points.")
    print("\nTotal scores are as follows:")
    print(f"Your total score is {score['You']} points.")
    high_score = score["You"]
    for n in range(1, 4):
        key = players[n]
        print(f"{key}'s total score is {score[key]} points.")
        if score[key] > high_score:
            high_score = score[key]
    for n in range(4):
        key = players[n]
        if score[key] == high_score:
            high_scorers.append(players[n])
    wait(1)
    if len(high_scorers) == 1:
        if high_scorers[0] == "You":
            print(f"\n{high_scorers[0]} are in the lead!")
        else:
            print(f"\n{high_scorers[0]} is in the lead!")
    elif len(high_scorers) == 2:
        print(f"\n{high_scorers[0]} and {high_scorers[1]} are", end="")
        print(" tied for the lead!")
    elif len(high_scorers) == 3:
        print(f"\n{high_scorers[0]}, {high_scorers[1]},", end="")
        print(f" and {high_scorers[2]} are tied for the lead!")
    elif len(high_scorers) == 4:
        print("\nEveryone is tied for the lead!")
    wait(1)
    return score, high_score


def declare_winner(scores):
    game_winner = ""
    high_score = 0
    print("We have a winner! Here are the final scores:\n")
    for player in players:
        print(player + ": " + str(scores[player]))
    for key in scores:
        if scores[key] > high_score:
            high_score = scores[key]
            game_winner = key
    clear()
    if game_winner == "You":
        print(f"\nYou win with a score of {high_score}!")
    else:
        print(f"\n{game_winner} wins with a score of {high_score}!")


version = "Version 0.0.2 (Alpha)"
players = ["You", "Yasmine", "Florian", "Sakura"]
order = []
main_deck = build_deck()
sh_list = build_shorthand(main_deck)
sh_dict = build_shorthand_dict(sh_list, main_deck)


def main():
    """Main body of the program"""
    main_menu()
    round = 1
    offset = random.randint(0, 3)
    order = get_order(round, players, offset)
    play_order = order[:]
    scoreboard = {"You": 0, "Yasmine": 0, "Florian": 0, "Sakura": 0}
    blind = {"You": False, "Yasmine": False, "Florian": False, "Sakura": False}
    highest_score = 0

    while highest_score < 300:
        # Performs one round of Spades
        clear()
        print(f"Beginning round {round}!")
        wait(0.5)
        shuffled_deck = shuffle_deck(main_deck)
        wait(0.5)
        print()
        player_hands = deal_cards(shuffled_deck)
        wait(0.5)
        player_hands[0] = sort_hand(player_hands[0], main_deck)
        print("\n...")
        wait()
        # while True:
        player_bids = [-1, -1, -1, -1]
        display_bids(player_bids, play_order)
        for i in range(4):
            if order[i] == "You":
                print()
                player_bids[0], blind = (
                    get_bid(player_hands[0], player_bids, play_order, blind))
                clear()
                display_bids(player_bids, play_order)
                wait()
            else:
                ind = players.index(order[i])
                player_bids[ind] = bot_bid(player_hands[ind])
                display_bids(player_bids, play_order)
                wait()
        wait()
        print("\n...\n")
        wait(1)
        spaded = False
# trick_pool and tricks_won order are static: [user, yasmine, florian, sakura]
        tricks_won = [0, 0, 0, 0]
        clear()
        display_tricks_won(tricks_won, player_bids)

        while player_hands[0]:
            # Initiates a trick for each card in players' hands
            trick_pool = ["", "", "", ""]
            first_card = ""
            print(f"\nTrick {14 - len(player_hands[0])}/13:\n")
            for player in play_order:
                wait()
                if player == "You":
                    while trick_pool[0] == "":
                        clear()
                        display_tricks_won(tricks_won, player_bids)
                        display_current_trick(
                            trick_pool, player_hands, play_order)
                        trick_pool[0] = (
                            user_play_card(player_hands[0], trick_pool,
                                           play_order, spaded, first_card)
                                            )
                    player_hands[0].remove(trick_pool[0])
                    if "Spades" in trick_pool[0]:
                        spaded = True
                else:
                    clear()
                    display_tricks_won(tricks_won, player_bids)
                    display_current_trick(trick_pool, player_hands, play_order)
                    index = players.index(player)
                    trick_pool[index] = (
                        bot_play_card(player_hands[index], trick_pool,
                                      player_bids[index],
                                      tricks_won[index], spaded,
                                      first_card)
                                        )
                    player_hands[index].remove(trick_pool[index])
                    if "Spades" in trick_pool[index]:
                        spaded = True
                clear()
                display_tricks_won(tricks_won, player_bids)
                display_current_trick(trick_pool, player_hands, play_order)
                if player == play_order[0]:
                        first_card = trick_pool[players.index(player)]
            wait()
            tricks_won, winner = (
                determine_winner(trick_pool, tricks_won, first_card))
            press_enter()
            clear()
            display_tricks_won(tricks_won, player_bids)
            winner_name = players[winner]
            win_ind = play_order.index(winner_name)
            play_order = play_order[win_ind:] + play_order[:win_ind]
        scoreboard, highest_score = (
            get_scores(scoreboard, tricks_won, player_bids, blind))
        round += 1
        order = order[1:] + order[:1]
        input("Press Enter to begin the next round!")
    return scoreboard

while True:
    scoreboard = main()
    declare_winner(scoreboard)
    press_enter()


print("\nThanks for playing!\n\n\n\n\n")
