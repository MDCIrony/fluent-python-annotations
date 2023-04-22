import collections
from random import choice
from typing import Generator

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __iter__(self, card_pos: int = 5) -> Generator:
        while True:
            new_choice = choice(self._cards)

            if new_choice == self._cards[card_pos]:
                break

            yield new_choice

    def get_random(self):
        return choice(self._cards)


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card: Card):
    rank_value = FrenchDeck.ranks.index(card.rank)

    return rank_value * len(suit_values) + suit_values[card.suit]
