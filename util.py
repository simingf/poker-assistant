import itertools
import math
from starting import get_hand_probabilities

hands = {0: "High Card", 1: "Pair", 2: "Two Pair", 3: "Three of a Kind", 4: "Straight", 5: "Flush", 6: "Full House", 7: "Four of a Kind", 8: "Straight Flush", 9: "Royal Flush"}

def print_probs_0(hand):
    probs = get_probs_0(hand)
    for i in range(10):
        # if probs[i] == 0:
        #     continue
        # else:
        print(hands[i] + ": " + str(round(probs[i] * 100, 2)) + "%")
    print()

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

def get_probs_0(hand):
    num_1 = to_num(hand[0][0])
    num_2 = to_num(hand[1][0])
    ace_1 = 1 if num_1 == 14 else num_1
    ace_2 = 1 if num_2 == 14 else num_2
    suit_1 = hand[0][1]
    suit_2 = hand[1][1]
    num_pair = (num_1 == num_2)
    suit_pair = (suit_1 == suit_2)

    total = math.comb(50, 5)

    # royal flush
    nums = [10, 11, 12, 13, 14]
    if num_1 in nums and num_2 in nums and num_1 != num_2:
        if suit_pair:
            royal_flush = 3 + math.comb(47, 2)
        else:
            royal_flush = 2 + 2 * 46
    elif num_1 in nums and num_2 in nums and num_pair:
        royal_flush = 2 + 2 * 46
    elif num_1 in nums or num_2 in nums:
        royal_flush = 3 + 46
    else:
        royal_flush = 4
    
    # straight flush
    straight_flush = 0
    for i in range(1, 11):
        nums = [i, i+1, i+2, i+3, i+4]
        if (num_1 in nums or ace_1 in nums) and (num_2 in nums or ace_2 in nums):
            if suit_1 == suit_2:
                straight_flush += 3 + math.comb(47, 2)
            else:
                straight_flush += 2 + 2 * 46
        elif (num_1 in nums or ace_1 in nums) or (num_2 in nums or ace_2 in nums):
            straight_flush += 3 + 46
        else:
            straight_flush += 4

    # 4 of a kind
    if num_pair:
        four_of_a_kind = 12 * 46 + math.comb(48, 3)
    else:
        four_of_a_kind = 11 * 46 + 2 * math.comb(47, 2)

    # full house
    if num_pair:
        full_house = 2 * 12 * math.comb(4, 2) * 44 * 40 / 2
        full_house += 12 * 4 * 44 * 40 / 2
    else:
        full_house = 11 * 4 * 10 * math.comb(4, 2)
        full_house += 3 * 11 * math.comb(4, 2) * 40
        full_house += 3 * 11 * 4 * 40
        full_house += 2 * 3 * 3 * 44 * 40 / 2

    # flush
    if suit_pair:
        flush = 3 * math.comb(13, 5)
        flush += math.comb(11, 3) * math.comb(39, 2)
    else:
        flush = 2 * math.comb(13, 5)
        flush += 2 * math.comb(12, 4) * 38

    # straight
    straight = 0
    for i in range(1, 11):
        nums = [i, i+1, i+2, i+3, i+4]
        if (num_1 in nums or ace_1 in nums) and (num_2 in nums or ace_2 in nums):
            straight += 3 * 3 * 4 * 4 * 4
            straight += 3 * 4 * 4 * 4 * 46
            straight += 4 * 4 * 4 * 47 * 46 / 2
        elif (num_1 in nums or ace_1 in nums) or (num_2 in nums or ace_2 in nums):
            straight += 3 * 4 * 4 * 4 * 4
            straight += 4 * 4 * 4 * 4 * 46
        else:
            straight += 4 * 4 * 4 * 4 * 4
    straight -= straight_flush

    # 3 of a kind
    if num_pair:
        three_of_a_kind = 12 * 4 * 44 * 40 / 2
        three_of_a_kind += math.comb(4, 2) * 48 * 44 * 40 * 36 / (4 * 3 * 2)
    else:
        three_of_a_kind = 11 * 4 * 40 * 36 / 2
        three_of_a_kind += 2 * 3 * 44 * 40 * 36 / (3 * 2)

    # 2 pair
    if num_pair:
        two_pair = math.comb(12, 2) * math.comb(4, 2) * math.comb(4, 2) * 40
        two_pair += 12 * math.comb(4, 2) * 44 * 40 * 36 / (3 * 2)
    else:
        two_pair = math.comb(11, 2) * math.comb(4, 2) * math.comb(4, 2) * 36
        two_pair += 2 * 3 * 11 * math.comb(4, 2) * 40 * 36 / 2
        two_pair += 3 * 3 * 11 * math.comb(4, 2) * 40
        two_pair += 3 * 3 * 44 * 40 * 36 / (3 * 2)

    # pair
    if num_pair:
        pair = 48 * 44 * 40 * 36 * 32 / (5 * 4 * 3 * 2)
    else:
        pair = 2 * 3 * 44 * 40 * 36 * 32 / (4 * 3 * 2)

    # high card
    if num_pair:
        high_card = 0
    else:
        high_card = 44 * 40 * 36 * 32 * 28 / (5 * 4 * 3 * 2)
    
    probs = [high_card, pair, two_pair, three_of_a_kind, straight, flush, full_house, four_of_a_kind, straight_flush, royal_flush]
    probs = [i / total for i in probs]
    return probs

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
