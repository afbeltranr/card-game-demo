class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f'{self.value}{self.suit}'



import random

class Deck:
    def __init__(self):
        suits = ['♠', '♣', '♥', '♦']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(value, suit) for suit in suits for value in values]
        random.shuffle(self.cards)  # Shuffle the deck
        self.discard_pile = []

    def draw_card(self):
        return self.cards.pop()

    def add_to_discard(self, card):
        self.discard_pile.append(card)

    def top_discard(self):
        return self.discard_pile[-1] if self.discard_pile else None