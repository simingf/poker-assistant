import math

def in_high_special_zone(card):
    if card[0] > 0:
        return True
    return False

def in_low_special_zone(card):
    if card[0] < 5:
        return True
    return False

def num_of_straight_flush(char):
    if (char == 'A' or char == 'K'):
        return 1
    elif (char == 2 or char == 'Q'):
        return 2
    elif (char == 3 or char == 'J'):
        return 3
    elif (char == 4 or char == 'T'):
        return 4
    return 5

def num_of_flushes(char):
    if (char == 'K'):
        return 1
    elif (char == 'A' or char == 2 or char == 'Q'):
        return 2
    elif char == 3 or char == 'J':
        return 3
    elif char == 4 or char == 'T':
        return 4
    else:
        return 5

""" only for when we have no cards in the river """
def get_hand_probabilities(hand):
    suits = ['c','d','h','s']
    answers = []
    total_combinations = math.comb(49,7)
    # Royal flush
    res = 0
    # case 1: both cards are 9 or below

    if  1<=hand[0][0]<=9 and 1<=hand[1][0]<=9:
        res = (4/total_combinations)
    # case 2: one card is above 9
    elif (1<=hand[0][0]<=9 and not(1<=hand[1][0]<=9)) or (not(1<=hand[0][0]<=9) and 1<=hand[1][0]<=9):
        #probability that we use another suit
        res += (3/total_combinations)
        #probability that we use the suit
        res += (49/total_combinations)
    # case 3: both cards are above 9
    else:
        # same suit
        if hand[0][1] == hand[1][1]:
            #we get it in another suit
            res += 3/total_combinations
            #we get it in the same suit
            res += math.comb(49,2)/ total_combinations
    answers.append(res)


    # Straight flush
    res = 0
    case = 0
    zone1 = in_high_special_zone(hand[0])
    zone2 = in_low_special_zone(hand[0])
    zone3 = in_high_special_zone(hand[1])
    zone4 = in_low_special_zone(hand[1])
    if (zone1 and zone3) or (zone2 and zone4):
        case = 1
    elif (zone1 and zone4) or (zone2 and zone3):
        case = 2
    elif (zone1 and zone2 and (not (zone3 or zone4))) or (zone3 and zone4 and (not (zone 1 or zone2))):
        case = 3
    else:
        case = 4
    # case 1: both cards in the same special zone
    if case == 1:
        # if suit is the same
        if (hand[0][1] == hand[1][1]):
            # we get it only using river cards
            res+= (3*9 + 9 - max_nums)/total_combinations
            # same suit
            max_nums = max(num_of_straight_flushes(hand[0][0]),num_of_straight_flushes(hand[1][0]))
            res += (max_nums * math.comb(47,2))/total_combinations
        else:
            case = 2

    # case 2: both cards in different special zones
    # case 3: only one card in one of the special zones
    if case == 2 or case == 3:
        # we get it only using river cards
        nums1 = num_of_straight_flushes(hand[0][0])
        nums2 = num_of_straight_flushes(hand[1][0])
        res+=(3*9 + 9 - nums1 - nums2)/total_combinations
        # we use cards in hand
        res+= 47 * (nums1 + nums2) / total_combinations

    # case 4: no cards in the special zone
    if case == 4:
        res+= 4*9/total_combinations
    answers.append(res)

    # 4 of a kind
    res = 0
    # case 1: if cards have the same number
    if (hand[0][0]==hand[1][0]):
        # only use river cards
        res+=12*math.comb(46,1)/total_combinations
        # use cards in hand
        res+=math.comb(48,3)/total_combinations
    # case 2: cards don't have the same number
    else:
        # only use river cards
        res+=11*math.comb(46,1)/total_combinations
        # use cards in hand
        res+=2*math.comb(47,2)/total_combinations
    answers.append(res)

    # Full house
    res = 0
    # Flush
    res = 0
    case = 0
    zone1 = in_high_special_zone(hand[0])
    zone2 = in_low_special_zone(hand[0])
    zone3 = in_high_special_zone(hand[1])
    zone4 = in_low_special_zone(hand[1])
    if (zone1 and zone3) or(zone2 and zone4):
        case = 1
    elif not (zone1 or zone2 or zone3 or zone4):
        case = 3
    else:
        case = 2

    # case 1: both in same special zone
    if case == 1:
        res+= (3*9 + 9 - max_nums)/total_combinations
        # same suit
        max_nums = max(num_of_straight_flushes(hand[0][0]),num_of_straight_flushes(hand[1][0]))
        res += (max_nums * math.comb(47,2))/total_combinations

    # case 2: in different special zones or only one in special zone
    if case == 2:
        num1 = num_of_flushes(hand[0])
        num2 = num_of_flushes(hand[1])
        # only use river cards
        res+=(10-num1-num2)

    # case 3: neither in special zones
    if case == 3:

    # minus straight flush and royal flush probability
    res -= answers[1]
    res -= answers[0]
    answers.append(res)


"""
def get_hand_probabilities(hand, river):
    answers = []
    cards = hand + river

    # Royal flush
    res = 0
    remaining = 7 - len(cards)
    possibles = {'c': 0, 'd': 0, 'h': 0, 's': 0}

    for card in cards:
        if card[1]=='T' or card[1]=='J' or card[1]=='Q' or card[1]=='K' or card[1]=='A':
            possibles[card[0]]+=1
    streaks = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    max_streak = 0
    for key in possibles:
        streaks[possibles[key]]+=1
        max_streak = max(max_streak, possibles[key])
    for streak in streaks:
        if remaining < (5-streak):
            res+=0
        else:
            res+= math.comb(52-cards,

    # Straight flush (excluding royal flush)

    # 4 of a kind

    # Full house

    # Flush (excluding royal and straight flush)

    # Straight

    # 3 of a kind

    # Two pair

    # One pair

    # No pair


def get_win_probabilities():
"""
