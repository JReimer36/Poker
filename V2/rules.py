from collections import Counter
from random import shuffle

def RANKS(): return ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
def SUITS(): return ['Clubs', 'Diamonds', 'Hearts', 'Spades']

value_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
hand_dict = {10: 'Royal Flush', 9: 'Straight Flush', 8: 'Four of a Kind', 7: 'Full House',
                   6: 'Flush', 5: 'Straight', 4: '3 of a Kind',
                   3: 'Two Pair', 2: 'Pair', 1: 'High Card'}
class Card:
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = value_dict.get(rank)
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.contents = [Card(rank, suit) for rank in RANKS() for suit in SUITS()]
        shuffle(self.contents)
        
    def shuffle(self):
        shuffle(self.contents)


class Deal(Deck):
    def __init__(self):
        super(Deal, self).__init__()
        self.deck = self.contents
    
    def remove_cards(self, lst):
        for card in lst:
            for value in self.deck:
                if (value.rank == card.rank) and (value.suit == card.suit):
                    self.deck.remove(value)
            else:
                pass
    def enter_cards(self, amt_cards):
        cards = []
        for x in range(amt_cards):
            print("\n Enter card rank")
            while True:
                print("Options: ")
                print([rank for rank in RANKS()])
                rank = input('>  ').title()
                if rank in RANKS():
                    break
                print("Please enter a valid option")
            print("\nEnter card suit")
            while True:
                print("Options: ")
                print([suit for suit in SUITS()])
                suit = input('> ').title()
                if suit in SUITS():
                    break
                print("Please enter a valid option")
            cards.append(Card(rank, suit))
        self.remove_cards(cards)
        return cards
            
    def deal(self):
        deal = self.enter_cards(2)
        return deal
    
    def flop(self):
        flop = self.enter_cards(3)
        return flop
    
    def turn(self):
        turn = self.enter_cards(1)
        return turn
    
    def river(self):
        river = self.turn()
        return river
    
    def show_deck(self):
        return (self.deck)
    
    def check_ranks(self):
        ranks = []
        for card in self.deck:
            ranks.append(card.rank)
        occurences = Counter(ranks)
        return occurences
    
    def check_suits(self):
        suits = []
        for card in self.deck:
            suits.append(card.suit)
        occurences = Counter(suits)
        return occurences
    
    def check_values(self):
        values = []
        for card in self.deck:
            values.append(card.value)
        occurences = Counter(values)
        return occurences

    def show_hand(self, lst):
        print("\nHand:")
        for card in lst:
            print(card, end=", ")

    def run_game(self):
        print("Start Game:")
        hand = []
        print("\nDeal")
        hand.extend(self.deal())
        self.show_hand(hand)
        print("\nFlop")
        hand.extend(self.flop())
        self.show_hand(hand)
        print("\nTurn")
        hand.extend(self.turn())
        self.show_hand(hand)
        print("\nRiver")
        hand.extend(self.river())
        self.show_hand(hand)


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

