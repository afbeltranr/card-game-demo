from src.game import Game, Player

def start_game():
    print("Welcome to the Card Game!")
    player_names = input("Enter player names (comma-separated): ").split(",")
    players = [Player(name.strip()) for name in player_names]
    game = Game(players)
    game.deal_cards()

    print("\nStarting the game...")
    while not game.is_over():
        for player in players:
            print(f"\n{player.name}'s turn:")
            print(f"Your hand: {player.hand}")
            print(f"Top card on discard pile: {game.discard_pile[-1]}")
            
            action = input("Choose an action - (1) Draw from deck, (2) Draw from discard pile, (3) Exchange cards: ")
            if action == '1':
                player.draw_card(game.deck)
            elif action == '2':
                player.draw_card(game.discard_pile, from_discard=True)
            elif action == '3':
                card_to_exchange = input("Enter the card you want to exchange: ")
                player.exchange_card(card_to_exchange, game.discard_pile)
            else:
                print("Invalid action. Turn skipped.")
            
            print(f"Your hand after action: {player.hand}")
            game.play_round()

    print("\nGame over! Here are the players' hands:")
    for player in players:
        print(f"{player.name}'s hand: {player.hand} - Score: {player.calculate_score()}")

if __name__ == "__main__":
    start_game()
