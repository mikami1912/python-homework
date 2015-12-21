import random
import math
type_card = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
type_kind = ['H', 'D', 'C', 'S']


def initialize_deck():
    input_deck = []
    for i_card in type_card:
        for i_kind in type_kind:
            input_deck.append(i_card + i_kind)
    return input_deck
        
def rank_hand(input_hand): # return a list with 3 elements (a,b,c) represent ranking of hand
    """
    if sf : a=8, b is high card, c=0
    if fk : a=7, b is card of 4 kind, c=0
    if fh : a=6, b is card of 3 kind, c=0
    if fl : a=5, b is card of high card, c=0
    if st : a=4, b is card of high card except A->5 and T->A, c=0
       b = 15, if T-A
       b = 14, if A-5
       b = 13, if 9-K
    if tk : a=3, b is card of 3 kind, c=0
    if tp : a=2, b is card of higher pair, c= card of lower pair
    if op : a=1, b is card of pair, c= highest kicker
    if hc : a=0, b is highest kicker, c=0
    """
    hand = split_hand(input_hand)
    ranking_hand = []
    if straight(input_hand) != None and flush(input_hand) != None: ranking_hand = [8, straight(input_hand)]      #sf
    elif kind(input_hand,4) != None: ranking_hand = [7, kind(input_hand,4)]                                      #fk
    elif kind(input_hand,3) != None and len(set(hand[0])) == 2: ranking_hand = [6, kind(input_hand,3)]           #fh
    elif flush(input_hand) != None: ranking_hand = [5, flush(input_hand)]                                           #fl
    elif straight(input_hand) != None: ranking_hand = [4, straight(input_hand)]                                  #st
    elif kind(input_hand,3) != None: ranking_hand = [3, kind(input_hand,3)]                                        #tk
    elif two_pair(input_hand) != None: ranking_hand = [2, two_pair(input_hand)]                                     #tp
    elif one_pair(input_hand) != None: ranking_hand = [1, one_pair(input_hand)]                                     #op
    else: ranking_hand = [0, max([int(i) for i in hand[0]], key=abs)]                                                                #hc
    return ranking_hand

def split_hand(input_hand): #take a hand and return list with 2 element. type card and type_kind
# example: input = ['7D', 'QH', '2D', '9D', '7C']
# output:
#   hand_split[0] = [7,Q,2,9,7] --> ['7','12','2','9','7']
#   hand_split[1] = [D,H,D,D,C]
    hand_split = [[],[]]    
    for item in input_hand:
        
        if item[0] == '1':
            hand_split[0].append('14')
        elif item[0] == 'K':
            hand_split[0].append('13')
        elif item[0] == 'Q':
            hand_split[0].append('12')
        elif item[0] == 'J':
            hand_split[0].append('11')
        elif item[0] == 'T':
            hand_split[0].append('10')
        else: hand_split[0].append(item[0])
        hand_split[1].append(item[1])
    return hand_split

def straight(input_hand): #take a hand and return the highest card in straight
#   input = ['TH', '6D', '7C', '9S', '8D' ] --> [10]
#   input = ['1C', 'QD', 'JC', 'TS', 'KH' ] --> [15]  (10-A)
#   input = ['2H', '3C', '4D', '5C', '1D' ] --> [14]  (1-5)
    hand = split_hand(input_hand)
    card_type = set([int(item) for item in hand[0]])
    if len(card_type) >= 5:
        for i in range(0,len(card_type)+1)
    else return None 
    
    
"""
    card_type.sort()
    hand_5 = [card_type[ele:ele+5] for ele in range(0,3)]
    print(card_type)
    print(hand_5)
    high_card_straight = []
    for set_hand in hand_5:
        if (max(set_hand)-min(set_hand) == 4) and len(set(set_hand)) == 5: # check if straight except 1-5 
            if max(set_hand) == 14: high_card_straight.append(15)
            else: high_card_straight.append(max(set_hand))
        elif set(set_hand) == {2,3,4,5} and card_type[6] == 14:
            high_card_straight.append(14)
        else: high_card_straight.append(0)
        print(high_card_straight, set(set_hand), card_type[6])
        
    if max(high_card_straight) !=0: return max(high_card_straight)
    else: return None
"""
def flush(input_hand): #take a hand and return 2 top high card in flush
    hand = split_hand(input_hand)
    high_card = int(0)
    next_high_card = int(0)
    if len(set(hand[1])) == 1:
        high_card = max([int(i) for i in hand[0]])
        hand[0].remove(str(high_card))
        next_high_card = max([int(i) for i in hand[0]])
        return high_card, next_high_card
    else: return None

def kind(input_hand, kind): # take a hand and number of kind to check and return . Only check for 3 kind and 4 kind. NOT for 2 kind
# example : kind(input_hand, 3) of 7A 7C 7D AC 9H --> return 7
    hand = split_hand(input_hand)
    for card in hand[0]:
        if hand[0].count(card) == kind: return int(card)
    return None

def two_pair(input_hand): # take a hand and return 2 card are the pair
    hand = split_hand(input_hand)
    pair_card = []
    if len(set(hand[0])) == 3 and kind(input_hand,3) == None:
        for card in hand[0]:
            if hand[0].count(card) == 2:
                pair_card.append(card)
        return max(int(i) for i in pair_card), min(int(i) for i in pair_card)
    else: return None

def one_pair(input_hand): # take a hand and return 2 card: card is a pair, and highest kicker
    hand = split_hand(input_hand)
    pair_card = ''
    high_kicker = ''
    if len(set(hand[0])) == 4:
        for card in hand[0]:
            if hand[0].count(card) == 2: pair_card = card
        hand[0].remove(pair_card)
        hand[0].remove(pair_card)
        return int(pair_card), max([int(i) for i in hand[0]], key=abs)       
    else: return None

def compare_hand(list_hand): #take input is a list of hand and return best hand
    return max(list_hand, key=rank_hand)
    

def test_list(number_of_hand): #return random list of number_of_hand to test
    output_list = []
    deck = initialize_deck()
    for i in range(0,number_of_hand-1):
        user_hand = random.sample(deck, 2)
        for j in user_hand: deck.remove(j)
        output_list.append(user_hand)
    pot = random.sample(deck,5)
    for i in output_list:
        i += pot 
    return output_list

def test():
    deck = initialize_deck()
    #t1 = random.sample(deck,7)
    t2 = ['1S', '2D', '3S', '4D', '5C', '4H', '4C']
    #print(t1)
    #hand = split_hand(t1)
    #print(hand)
    #print(max([int(i) for i in hand[0]], key=abs)) #test high card: OK
    print(straight(t2)) #test straight : 
    #print(two_pair(t2)) #test two_pair : OK
    #print(t2, '-->', one_pair(t2),) #test one_pair: OKmax([int(i) for i in hand[0]], key=abs)
    #print(kind(t2,3)) #test kind 3 and 4: OK
    #print(rank_hand(t2)) #test rank_hand
"""
    j = 0
    while j < 5:
        list_to_test = test_list(10)
        for i in list_to_test:
            print(i,'-->',rank_hand(i))
        print('Best_hand:',compare_hand(list_to_test))
        j += 1   
"""
    
test()
        
    
    
    


