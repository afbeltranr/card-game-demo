# test_game.py

from src.game import Player, Game
from src.card import Deck, Card

def test_player_initialization():
    player = Player("Alice")
    assert player.name == "Alice"
    assert len(player.hand) == 0  # Should start with an empty hand

def test_player_draw_from_deck():
    player = Player("Alice")
    deck = Deck()
    drawn_card = player.draw_from_deck(deck)
    assert isinstance(drawn_card, Card)
    assert len(deck.cards) == 51  # After drawing, there should be 51 cards left

def test_player_exchange_card():
    player = Player("Alice")
    player.hand = [Card(3, '♠'), Card(7, '♥'), Card(2, '♦'), Card('J', '♣')]
    new_card = Card(1, '♣')  # This card has a lower value than 7♥
    discarded_card = player.exchange_card(1, new_card)
    assert discarded_card.value == 7
    assert player.hand[1].value == 1

def test_game_deal_cards():
    players = [Player("Alice"), Player("Bob")]
    game = Game(players)
    game.deal_cards()
    for player in players:
        assert len(player.hand) == 4  # Each player should have 4 cards

def test_game_take_turn():
    players = [Player("Alice"), Player("Bob")]
    game = Game(players)
    game.deal_cards()
    game.take_turn(players[0])
    assert len(players[0].hand) == 4  # The player's hand should remain at 4 cards after exchanging
    assert len(game.deck.discard_pile) == 1  # After a turn, there should be one card in the discard pile
