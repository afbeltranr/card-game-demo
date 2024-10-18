class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []  # Contains four cards: two face-up and two face-down
        self.score = 0
        self.is_active = True  # Indicates whether the player is active
        self.is_winner = False  # Indicates whether the player is the winner

    def deal_initial_hand(self, deck):
            """Deals initial four cards to the player's hand: 2 face-up and 2 face-down."""
            self.hand = [deck.draw_card() for _ in range(4)]

    def draw_from_deck(self, deck):
        """Draws a card from the deck that is different from the cards in the player's hand."""
        while True:
            drawn_card = deck.draw_card()
            if all(drawn_card.value != card.value or drawn_card.suit != card.suit for card in self.hand):
                return drawn_card
    
    def draw_from_discard(self, deck):
        """Draws the top card from the discard pile."""
        return deck.draw_card()  # Fix: Remove the card from the discard pile
    
    def exchange_card(self, card_index, new_card):
        """Exchanges a card in the player's hand with a new card if it lowers the score."""
        current_card = self.hand[card_index]
        if self.card_value(new_card) < self.card_value(current_card):
            self.hand[card_index] = new_card
            return current_card
        else:
            return new_card

    def card_value(self, card):
        """Returns the value of a card for scoring purposes."""
        if card.value in ['J', 'Q']:
            return 10
        elif card.value == 'K':
            return 0 if card.color == 'red' else 20
        elif card.value == 'A':
            return 1  # Assign a value for Ace
        else:
            return int(card.value)  # Ensure integer comparison

    def calculate_score(self):
        """Calculates the score based on the card values and colors."""
        score = 0
        for card in self.hand:
            score += self.card_value(card)
        return score

from src.card import Deck

class Game:
    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.current_turn = 0
        self.game_ended = False
        self.deal_cards()  # Deal initial cards when the game starts
    
    def deal_cards(self):
        """Deals initial four cards to each player: 2 face-up and 2 face-down."""
        for player in self.players:
            # Each player gets four cards
            player.hand = [self.deck.draw_card() for _ in range(4)]
    
    def take_turn(self, player):
        """Handles a player's turn: draw, exchange, and manage special rules."""
        print(f"{player.name}'s turn.")
        # Let's assume player always draws from the deck for now
        drawn_card = player.draw_from_deck(self.deck)
        print(f"{player.name} drew a {drawn_card}")
        
        # Exchange the drawn card with one from the hand (simplified logic)
        discarded = player.exchange_card(0, drawn_card)  # Replace card at index 0 for example
        self.deck.add_to_discard(discarded)
        print(f"{player.name} discarded {discarded}")
    
    def play_round(self):
        """Plays one round of the game, where each player gets one turn."""
        for player in self.players:
            self.take_turn(player)
            if self.check_end_condition(player):
                break
    
    def check_end_condition(self, player):
        """Check if a player calls for the game end."""
        # Simplified end condition for now (can be expanded later)
        return False