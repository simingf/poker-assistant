import math

def in_high_special_zone(card):
    if int(card[0][0]) > 0:
        return True
    return False

def in_low_special_zone(card):
    if int(card[0][0]) < 5:
        return True
    return False

def num_of_straight_flushes(char):
    if (char == 'A' or char == 'K'):
        return 1
    elif (char == 2 or char == 'Q'):
        return 2
    elif (char == 3 or char == 'J'):
        return 3
    elif (char == 4 or char == 'T'):
        return 4
    return 5

def num_of_straights(char):
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
    answers = []
    total_combinations = math.comb(50,5)

    # Royal flush   
    res = 0
    # case 1: both cards are 9 or below
    first = int(hand[0][0])
    second = int(hand[1][0])
    if  1<=first<=9 and 1<=second<=9:
        res = (4/total_combinations)
    # case 2: one card is above 9
    elif (1<=first<=9 and not(1<=second<=9)) or (not(1<=first<=9) and 1<=second<=9):
        #probability that we use another suit
        res += (3/total_combinations)
        #probability that we use the suit
        res += (46/total_combinations)
    # case 3: both cards are above 9
    else:
        # same suit
        if hand[0][1] == hand[1][1]:
            #we get it in another suit
            res += 3 / total_combinations
            #we get it in the same suit
            res += math.comb(47,2) / total_combinations
        # different suits
        else:
            res += 2 * 48 / total_combinations
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
    elif (zone1 and zone2 and (not (zone3 or zone4))) or (zone3 and zone4 and (not (zone1 or zone2))):
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
            max_nums = max(num_of_straight_flushes(hand[0][0]), num_of_straight_flushes(hand[1][0]))
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

    # case 1: pair in hand
    if hand[0][0] == hand[1][0]:
        # form the 3 using hand
        res += 2 * 12 * math.comb(4,2) * 44 * 40 / (2 * total_combinations)
        # use hand as pair
        res += 12 * 4 * 44 * 40 / (2*total_combinations)
    else:
        # only using river
        res += 11 * 4 * 10 * math.comb(4,2) / total_combinations
        # only using 1 card for 3
        res += 3 * 11 * math.comb(4,2) * 40 / total_combinations
        # only using 1 card for pair
        res += 3 * 11 * 4 * 40 / total_combinations
        # use one card for 3, one card for pair
        res += 2 * 3 * 3 * 44 * 40 / (2* total_combinations)

    answers.append(res)

    # Flush
    res = 0
    # if both cards in hand have the same suit
    if hand[0][1] == hand[1][1]:
        # only use river cards
        res += 4 * math.comb(13,5) / total_combinations
        # use cards in hand
        res += math.comb(11,3) * math.comb(47,2) / total_combinations
    # cards in have have different suit
    else:
        # only use river cards
        res += 2 * math.comb(13,5) / total_combinations
        # use cards in hand
        res += 2 * 46 / total_combinations
    answers.append(res)

    # Straight
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
        max_nums = max(num_of_straights(hand[0][0]),num_of_straights(hand[1][0]))
        res += (3 * 9 + 9 - max_nums) / total_combinations
        # same suit
        res += (max_nums * math.comb(47,2))/total_combinations

    # case 2: in different special zones or only one in special zone
    # or case 3: neither in special zones
    if case == 2:
        num1 = num_of_straights(hand[0])
        num2 = num_of_straights(hand[1])
        # only use river cards
        res+= (10-num1-num2) * (4**5)/total_combinations
        # use cards
        res+= (num1+num2) * (4**4) * 46 / total_combinations

    # minus straight flush and royal flush probability
    res -= answers[1]
    res -= answers[0]
    answers.append(res)

    # 3 of a kind
    res = 0
    # case 1: cards in hand have the same number
    if hand[0][0] == hand[1][0]:
        # only use river cards:
        res += 12 * math.comb(47,2) / total_combinations
        # use cards in hand:
        res += 2* math.comb(49, 4) / total_combinations
    # case 2: cards in hand have different number
    else:
        # only use river cards:
        res += 12 * math.comb(47,2) / total_combinations
        # use cards in hand:
        res += 2 * math.comb(3,2) * math.comb(48,3) / total_combinations

    # subtract 4 of a kind probability
    res-=answers[2]
    answers.append(res)

    # 2 pair
    res = 0
    # case 1: have pair in hand
    if hand[0][0] == hand[1][0]:
        res = 12 * math.comb(4,2) * math.comb(46,3) / total_combinations
    # case 2: don't have pair in hand
    else:
        # only using river cards
        res += math.comb(11,2) * math.comb(4,2) * math.comb(4,2) * 42 / total_combinations
        # use one card in hand
        res += 2 * 3 * 11 * math.comb(4,2) * math.comb(43,2) / total_combinations
        # use both cards in hand
        res += 3 * 3 * math.comb(44,3) / total_combinations

    # subtract 4 of a  kind
    res -= answers[2]
    answers.append(res)
    # 1 pair
    res = 0
    # case 1: hand is pair
    if hand[0][0] == hand[1][0]:
        # river cards don't have a pair
        res = 48 * 44 * 40 * 36 * 32 / (total_combinations * 120)
    # case 2: hand is not pair
    else:
        # only use river cards
        res += 11 * math.comb(4,2) * 40 * 36 * 32 / (total_combinations * 6)
        # use one of the hand cards
        res += 2 * 3 * 44 * 40 * 36 * 32 / (total_combinations * 24)
    answers.append(res)

    # high card
    res = 0
    if not (hand[0][0] == hand[1][0]):
        res = 44 * 40 * 36 * 32 * 28 / (total_combinations * 120)
    answers.append(res)

    return answers


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
