from util import print_probs_0, print_probs_3, print_probs_4, print_probs_5

def play_round():
    num_players = get_num_players()
    if num_players == 'q' or num_players == 'n':
        return num_players
    player_hand = get_cards("Enter your hand (2 cards)", 2)
    if player_hand == 'q' or player_hand == 'n':
        return player_hand
    river = []
    print_state(player_hand, river)
    print_probs_0(player_hand)
    new_cards = get_cards("Enter the first 3 cards of the river", 3)
    if new_cards == 'q' or new_cards == 'n':
        return new_cards
    river += new_cards
    print_state(player_hand, river)
    print_probs_3(player_hand, river)
    new_cards = get_cards("Enter the 4th card of the river", 1)
    if new_cards == 'q' or new_cards == 'n':
        return new_cards
    river += new_cards
    print_state(player_hand, river)
    print_probs_4(player_hand, river)
    new_cards = get_cards("Enter the last card of the river", 1)
    if new_cards == 'q' or new_cards == 'n':
        return new_cards
    river += new_cards
    print_state(player_hand, river)
    print_probs_5(player_hand, river)
    return 'n'

def get_num_players():
    num_players = input("How many players? (2-10) \n")
    if num_players == "q":
        return "q"
    elif num_players == "n":
        return "n"
    else:
        try:
            num_players = int(num_players)
            if num_players < 2 or num_players > 10:
                print("Invalid input")
                return get_num_players()
            return num_players
        except ValueError:
            print("Invalid input")
            return get_num_players()

def get_cards(prompt, num_cards):
    player_hand = input(prompt + " (\"h\" for help) \n")
    if player_hand == "q":
        return "q"
    elif player_hand == "n":
        return "n"
    elif player_hand == "h":
        print("Card numbers are 23456789TJQKA")
        print("Card suits are cdhs")
        print("Example: \"As Kd\"")
        return get_cards(prompt, num_cards)
    else:
        try:
            player_hand = str(player_hand).split()
            if len(player_hand) != num_cards:
                print("Invalid input")
                return get_cards(prompt, num_cards)
            for card in player_hand:
                if len(card) != 2 or card[0] not in "23456789TJQKA" or card[1] not in "cdhs":
                    print("Invalid input")
                    return get_cards(prompt, num_cards)
            return player_hand
        except ValueError:
            print("Invalid input")
            return get_cards(prompt, num_cards)

def print_state(hand, river):
    print("Your hand: " + str(hand))
    print("River: " + str(river))

if __name__ == "__main__":
    print("Type \"n\" to start a new round")
    print("Type \"q\" to quit")
    total_rounds = 1
    while True:
        print("Round " + str(total_rounds))
        res = play_round()
        if res == "q":
            break
        elif res == "n":
            total_rounds += 1