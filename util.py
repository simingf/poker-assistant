import itertools

hands = {0: "High Card", 1: "Pair", 2: "Two Pair", 3: "Three of a Kind", 4: "Straight", 5: "Flush", 6: "Full House", 7: "Four of a Kind", 8: "Straight Flush", 9: "Royal Flush"}

def print_probs_3(hand, river):
    probs = get_probs_3(hand, river)
    for i in range(10):
        if probs[i] == 0:
            continue
        else:
            print(hands[i] + ": " + str(round(probs[i] * 100, 2)) + "%")
    print()

def print_probs_4(hand, river):
    probs = get_probs_4(hand, river)
    for i in range(10):
        if probs[i] == 0:
            continue
        else:
            print(hands[i] + ": " + str(round(probs[i] * 100, 2)) + "%")
    print()

def print_probs_5(hand, river):
    probs = get_probs_5(hand, river)
    for i in range(10):
        if probs[i] == 0:
            continue
        else:
            print(hands[i] + ": " + str(round(probs[i] * 100, 2)) + "%")
    print()

def get_probs_3(hand, river):
    count = 0
    hands_count = {}
    known_cards = hand + river
    for i in "23456789TJQKA":
        for i_s in "cdhs":
            for j in "23456789TJQKA":
                for j_s in "cdhs":
                    if i + i_s not in hand and i + i_s not in river and j + j_s not in hand and j + j_s not in river and i + i_s != j + j_s:
                        count += 1
                        cards = known_cards + [i + i_s, j + j_s]
                        hands_count[best_hand(cards)] = hands_count.get(best_hand(cards), 0) + 1
    probs = []
    for i in range(10):
        probs.append(hands_count.get(i, 0) / float(count))
    return probs

def get_probs_4(hand, river):
    count = 0
    hands_count = {}
    known_cards = hand + river
    for i in "23456789TJQKA":
        for i_s in "cdhs":
            if i + i_s not in hand and i + i_s not in river:
                count += 1
                cards = known_cards + [i + i_s]
                hands_count[best_hand(cards)] = hands_count.get(best_hand(cards), 0) + 1
    probs = []
    for i in range(10):
        probs.append(hands_count.get(i, 0) / float(count))
    return probs

def get_probs_5(hand, river):
    cards = hand + river
    index = best_hand(cards)
    res = [0] * 10
    res[index] = 1
    return res

def best_hand(hand):
    assert(len(hand) == 7)

    best = 0
    for subset in itertools.combinations(hand, 5):
        best = max(best, evaluate_hand(subset))
    return best

def evaluate_hand(hand):
    assert(len(hand) == 5)

    suits = [card[1] for card in hand]
    flush = False
    for suit in suits:
        if suits.count(suit) == 5:
            flush = True

    straight = False
    royal = False
    numbers = [to_num(card[0]) for card in hand]
    if 14 in numbers:
        numbers += [1]
    for i in range(1, 11):
        if i in numbers and i+1 in numbers and i+2 in numbers and i+3 in numbers and i+4 in numbers:
            straight = True
            if i == 10:
                royal = True

    if royal and flush and straight:
        return 9
    elif flush and straight:
        return 8

    for card in numbers:
        if numbers.count(card) == 4:
            return 7
        elif numbers.count(card) == 3:
            for card2 in numbers:
                if numbers.count(card2) == 2:
                    return 6

    if flush:
        return 5

    if straight:
        return 4

    for card in numbers:
        if numbers.count(card) == 3:
            return 3
        elif numbers.count(card) == 2:
            for card2 in numbers:
                if numbers.count(card2) == 2 and card != card2:
                    return 2
            return 1

    return 0

def to_num(card):
    if card == "T":
        return 10
    elif card == "J":
        return 11
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    elif card == "A":
        return 14
    else:
        return int(card)

if __name__ == "__main__":
    print(best_hand(["As", "Ks", "Qs", "Js", "Ts", "9s", "8s"]))
    print(best_hand(["As", "2s", "3s", "4s", "5s", "9s", "8d"]))
    print(best_hand(["As", "Ad", "Ah", "Ac", "6s", "6d", "8c"]))
    print(best_hand(["As", "Ad", "Ah", "3d", "6s", "6d", "8c"]))
    print(best_hand(["3h", "5h", "Ah", "Jh", "6h", "6d", "8c"]))
    print(best_hand(["3h", "4d", "5h", "6c", "7d", "6d", "8c"]))
    print(best_hand(["3h", "3d", "3c", "Jh", "5h", "6d", "8c"]))
    print(best_hand(["3h", "3d", "7c", "Jh", "6h", "6d", "8c"]))
    print(best_hand(["3h", "3d", "7c", "Jh", "6h", "9d", "8c"]))
    print(best_hand(["2h", "3d", "7c", "Jh", "6h", "9d", "8c"]))
