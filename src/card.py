class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f'{self.value}{self.suit}'



class Deck:
    def __init__(self):
        suits = ['♠', '♣', '♥', '♦']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def draw_card(self):
        return self.cards.pop()