import random

class Card:

    _rank_order = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, r = "None", s = "None"):
        self._rank = r
        self._suit = s
        
    def display(self):
        print(self._rank, "of", self._suit)

    def beats(self, other):
        order = Card._rank_order
        try:
            pos_self = order.index(self._rank)
            pos_other = order.index(other._rank)
            return pos_self > pos_other
        except:
            raise BreakShanesCode("WHY MUST YOU BREAK MY CODE")
                                 

class Deck:
    _ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    _suits = ["Hearts", "Clubs", "Diamonds", "Spades"]

    def __init__(self):
        self._cards_left = 52
        self._cards = []
        for r in Deck._ranks:
            for s in Deck._suits:
                self._cards.append(Card(r,s))
        # The "Knuth Shuffle"
        for i in range(52):
            j = random.randrange(i,52)
            temp = self._cards[i]
            self._cards[i] = self._cards[j]
            self._cards[j] = temp
        
    def draw(self):
        if self._cards_left > 0:
            self._cards_left -= 1
            # .pop() takes a list, and simultaneously returns its last element,
            # and removes that element from the list.
            return self._cards.pop()
        else:
            raise BreakShanesCode("WANTED TO SEE WHAT WOULD HAPPEN, DID YOU?")
    
class BreakShanesCode(Exception):
    pass
        
