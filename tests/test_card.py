# test_card.py

from src.card import Card, Deck

def test_card_creation():
    card = Card(5, '♠')
    assert card.value == 5
    assert card.suit == '♠'
    assert str(card) == '5♠'

def test_deck_creation():
    deck = Deck()
    assert len(deck.cards) == 52  # A standard deck with 52 cards (1-10, J, Q, K, A in four suits)

def test_draw_card():
    deck = Deck()
    card = deck.draw_card()
    assert isinstance(card, Card)
    assert len(deck.cards) == 51  # After drawing a card, there should be 51 left

def test_discard_pile():
    deck = Deck()
    card = deck.draw_card()
    deck.add_to_discard(card)
    assert deck.top_discard() == card  # The top of the discard pile should be the card that was added