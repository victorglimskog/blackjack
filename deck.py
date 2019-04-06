'''
Deck and Card classes.
'''
from random import shuffle

class Deck():
    '''
    Deck consists of 52 cards that is created on init.
    It can be shuffled and it can deal the next card
    '''
    def __init__(self):
        suites = ('h', 'd', 's', 'c')
        values = tuple(range(2,11)) + ('J','Q','K','A')
        self.deck = []
        for value in values:
            for suite in suites:
                self.deck.append(f'{value}{suite}')
        self.shuffle()

    def shuffle(self):
        shuffle(self.deck)

    def next_card(self):
        return self.deck.pop()


class Card():
    '''
    Each card have a suit and a value.
    '''
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def __str__(self):
        return f'{self.suite}{self.value}'
