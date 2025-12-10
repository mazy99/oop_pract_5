#!/usr/bin/env python3
# -*- coding: utf-8 -*


from dataclasses import dataclass, field

RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
SUITS = "♠ ♥ ♦ ♣".split()


def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


@dataclass
class PlayingCard:
    rank: str
    suit: str


@dataclass
class Deck:
    cards: list[PlayingCard] = field(default_factory=make_french_deck)


def main():
    deck = Deck()
    print("Вся колода:")
    print(deck)

    print("\nКарты в колоды:")
    for card in deck.cards[:52]:
        print(card)


if __name__ == "__main__":
    main()
