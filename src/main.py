# main.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.card import Deck, Card
from src.game import Game, Player

def display_hand(player):
    print(f"{player.name}'s hand: {[str(card) for card in player.hand]}")

def main():
    print("Welcome to the Card Game Demo!")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    players = [player]
    game = Game(players)

    while True:
        print("\nOptions:")
        print("1. Draw a card")
        print("2. Discard a card")
        print("3. View hand")
        print("4. End turn")
        print("5. Quit game")

        choice = input("Choose an option: ")

        if choice == '1':
            card = player.draw_from_deck(game.deck)
            print(f"You drew: {card}")
        elif choice == '2':
            display_hand(player)
            card_index = int(input("Enter the index of the card to discard: "))
            discarded_card = player.exchange_card(card_index, None)
            game.deck.add_to_discard(discarded_card)
            print(f"You discarded: {discarded_card}")
        elif choice == '3':
            display_hand(player)
        elif choice == '4':
            print("Ending turn...")
            game.take_turn(player)
        elif choice == '5':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()