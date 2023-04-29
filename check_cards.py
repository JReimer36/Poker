from collections import Counter

def nMax(lst, N): 
    final_list = [] 
    
    for i in range(0, N):  
        max1 = 0
          
        for j in range(len(lst)):      
            if lst[j] > max1: 
                max1 = lst[j]; 
                  
        lst.remove(max1); 
        final_list.append(max1) 
          
    return (final_list)

def check_pair(hand):
    ranks = []
    result = []
    for card in hand:
        ranks.append(card.rank)
    occurences = Counter(ranks)
    max_value = max(list(occurences.values()))
    if max_value >= 2:
        result.append(1)
        result.append(0)
    else:
        result.append(round((max_value/2), 2))
        result.append(2-max_value)
    return result


def check_2pair(hand):
    ranks = []
    result = []
    for card in hand:
        ranks.append(card.rank)
    occurences = Counter(ranks)
    rank_count = list(occurences.values())
    pair_count = 0
    for i in rank_count:
        if i >= 2:
            pair_count += 1
    if pair_count >= 2:
        result.append(1)
        result.append(0)
    else:
        result.append(round((pair_count/2), 2))
        result.append(3-(pair_count*2))
    return result


def check_3kind(hand):
    ranks = []
    result = []
    for card in hand:
        ranks.append(card.rank)
    occurences = Counter(ranks)
    max_value = max(list(occurences.values()))
    if max_value >= 3:
        result.append(1)
        result.append(0)
    else:
        result.append(round((max_value/3), 2))
        result.append(3-max_value)
    return result

def check_straight(hand):
    # Create all set variations
    straight_list = []
    for x in range(2, 11):
        straight_list.append(list(range(x, x+5)))
    # Test what straight variations are possible with hand
    values = []
    result = []
    for card in hand:
        values.append(card.value)
    values.sort()
    similarities = []
    for group in straight_list:
         similarities.append(list(set(values).intersection(group)))
    # Amt of cards closest to a straight
    max_value = len(max(similarities))
    if max_value >= 5:
        result.append(1)
        result.append(0)
    else:
        result.append(max_value/5)
        result.append(5 - max_value)
    return result

def check_flush(hand):
    suits = []
    result = []
    if bool(hand):
        for card in hand:
            suits.append(card.suit)
        occurences = Counter(suits)
        max_value = max(list(occurences.values()))
        if max_value >= 5:
            result.append(1)
            result.append(0)
        else:
            result.append(round((max_value/5), 2))
            result.append(5-max_value)
    else:
        result.append(0)
        result.append(5)
    return result

def check_fullhouse(hand):
    ranks = []
    result = []
    for card in hand:
        ranks.append(card.rank)
    occurences = Counter(ranks)
    max_values = (list(occurences.values()))
    if len(max_values) == 1:
        result.append(0)
        result.append(3)
    else:
        top2 = nMax(max_values, 2)
        check_first = 3 - top2[0]
        check_second = 2 - top2[1]
        total = check_first + check_second
        if total == 0:
            result.append(1)
            result.append(0)
        else:
            result.append(round(((5-total)/5), 2))
            result.append(total)
    return result

def check_4kind(hand):
    ranks = []
    result = []
    for card in hand:
        ranks.append(card.rank)
    occurences = Counter(ranks)
    max_value = max(list(occurences.values()))
    if max_value == 4:
        result.append(1)
        result.append(0)
    else:
        result.append(round((max_value/4), 2))
        result.append(4-max_value)
    return result

def check_straightflush(hand):
    suits = []
    refined_hand = []
    for card in hand:
        suits.append(card.suit)
    occurences = Counter(suits)
    max_value = max(list(occurences.values()))
    for x, count in occurences.items():
        if count == max_value:
            current_suit = x
    for card in hand:
        if card.suit == current_suit:
            refined_hand.append(card)
        else:
            pass
    checkstraight = check_straight(refined_hand)
    return checkstraight

def check_royalflush(hand):
    filtered_hand = []
    for card in hand:
        if card.value >= 10 and card.value <= 14:
            filtered_hand.append(card)
    checkflush = check_flush(filtered_hand)
    return checkflush