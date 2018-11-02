import collections

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._card = [Card(rank,suit) for suit in self.suits
        for rank in self.ranks]
    
    def __len__(self):
        return len(self._card)
    
    def __getitem__(self,position):
        return self._card[position]

suit_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

from math import hypot

class Vector:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'Vector(%,%r)' % (self.x,self.y)
    
    def __abs__(self):
        return hypot(self.x,self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self,orther):
        x = self.x + orther.x
        y = self.y + orther.y
        return Vector(x,y)
    
    def __mul__(self,scalar):
        return Vector(self.x * scalar, self.y * scalar)