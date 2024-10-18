import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.color = 'red' if suit in ['♥', '♦'] else 'black'
    
    def __repr__(self):
        return f"Card(value='{self.value}', suit='{self.suit}', color='{self.color}')"
    
    def __str__(self):
        return f"Card: {self.value} of {self.suit} ({self.color})"




class Deck:
    def __init__(self):
        # Create a standard deck of cards (values 1-10, J, Q, K, A for simplicity)
        self.cards = [Card(value, suit) for value in list(range(1, 11)) + ['J', 'Q', 'K', 'A'] 
                      for suit in ['♠', '♥', '♦', '♣']]
        random.shuffle(self.cards)
        self.discard_pile = []
        
    def draw_card(self):
        """Draws a card from the top of the deck."""
        if not self.cards:
            self.reshuffle()
        return self.cards.pop()
    
    def reshuffle(self):
        """Reshuffles the discard pile back into the deck."""
        self.cards = self.discard_pile
        self.discard_pile = []
        random.shuffle(self.cards)
    
    def add_to_discard(self, card):
        """Adds a card to the discard pile."""
        self.discard_pile.append(card)
    
    def top_discard(self):
        """Returns the top card of the discard pile without removing it."""
        return self.discard_pile[-1] if self.discard_pile else None