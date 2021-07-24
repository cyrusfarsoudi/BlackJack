import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + " of " + self.suit

    def getRank(self):
        return self.rank

    def graphicPrint(self):
        print('┌───────┐')
        print(f'| {self.rank:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.rank:>2} |')
        print('└───────┘') 

class Deck:
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    symbols = ['♥', '♦', '♣', '♠']

    def __init__(self, useSymbols=True):
        self.liveCards = []
        self.deadCards = []
        self.build(useSymbols)

    def build(self, useSymbols):
        if(useSymbols):
            suits = Deck.symbols
        else:
            suits = Deck.suits

        for rank in Deck.ranks:
                for symbol in suits:
                    self.liveCards.append(Card(rank, symbol))

        self.shuffle()

    def print(self, graphical=False):
        for card in self.liveCards:
            card.graphicPrint() if graphical else print(card)

    def shuffle(self):
        random.shuffle(self.liveCards)

    def reset(self):
        self.liveCards += self.deadCards
        self.deadCards.clear()

    def draw(self, num=1):
        cards = []
        for i in range(num):
            cards.append(self.liveCards.pop(0))
        return cards


