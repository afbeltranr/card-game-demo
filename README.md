# 🃏 Card Game Demo Project

Welcome to the **Card Game Demo** project! This project aims to build a simple yet engaging card game using Python. The focus is on creating a text-based game that can later be expanded with a dynamic dashboard for visualizations and potentially multiplayer functionality.

## 🎯 Project Overview
In this card game, players draw from either a **pile of unknown cards** or a **pile of known discarded cards**. The goal is to **achieve the lowest score** based on the values of cards in hand, with special scoring rules for certain cards:

- Red King ♔ = 0 points
- Black King ♚ = 20 points
- Other cards = their face value (e.g., 2-10, J, Q)

### 🔄 Starting Conditions
- Each player begins with **four random cards**:
  - **Two cards are known** to the player (face-up).
  - **Two cards are unknown** (face-down).

### 🔄 Turn-Based Actions
- On each turn, a player must:
  - Select a card from either the **known discard pile** or the **unknown draw pile**.
  - **Exchange** the drawn card for one of the four cards in their own hand.
- The player can choose to swap the new card with one of their face-up or face-down cards.

### 🔚 Game End Condition
- A player can **make a call** if they believe they have the **lowest score** at the table. This call can only be made during their own turn.
- After a call is made:
  - All other players get **one last turn**.
  - The game ends once the turn of the player who goes right before the caller is completed.
  - Everyone then reveals their cards.
- The player with the **highest score** loses the round and will start the next round with **one extra card** (making it more difficult to achieve a low score).

### 📝 Special Rules
- **Matching a Q**: If a player plays a **Queen (Q)** that matches the last discarded **Q**, they can cut the turn and gain a special power:
  - They are allowed to **peek** at one of their own **unknown cards** (face-down).
  - After peeking, they must choose whether to **keep the peeked card** or **exchange it** with a card from the known or unknown decks.
  - Regardless of their decision, they must **exchange a card** after peeking.
- **Matching a J with a J**: If a player matches the last discarded **Jack (J)** with their own **J**, they cut the next player’s turn and gain a special power:
  - They can **swap one card** from their own set with a card from another player's set.
  - This power can be used strategically if they have knowledge of a high-value card in another player’s hand.
- These special rules add an element of **strategy** and **timing**, making the game more dynamic and competitive.

## 📚 PACE Methodology
This project follows the **PACE** methodology, which ensures a structured approach to development:

### 1. 📝 Plan
- Define game rules, mechanics, and objectives.
- Set up a **GitHub repository** and environment for development.
- Outline clear **milestones** and **goals** for each stage.

### 2. 🔍 Analyze
- Break down game mechanics and interactions.
- Identify **user data points** to track during gameplay:
  - Choices made by the player (e.g., known vs. unknown pile).
  - Timing of actions (e.g., time taken to draw).
  - Actions using special rules like **Q peeks** and **J swaps**.
- Plan data storage and analysis methods (e.g., using pandas for tracking).

### 3. 🛠️ Construct
- Build the core game components:
  - **Card Class**: Represents a card with its number, suit, and color.
  - **Deck Class**: Manages the deck, draw pile, and discard pile.
  - **Game Logic**: Implements player turns, drawing, discarding, and scoring.
  - **Special Rule Logic**: Implements the behaviors for **Q peeks** and **J swaps**.
- Write initial tests to ensure functionality and flow.

### 4. 🚀 Execute
- Create a **Command-Line Interface (CLI)** for player interaction.
- Simulate and test playthroughs, adjusting logic based on feedback.
- Start basic **data analysis** on user choices and gameplay patterns.
- Plan for a future **dynamic dashboard** to visualize game states.

## 🗂️ Project Structure
The project is organized to facilitate **data analysis** and **game development**. Here is the intended folder structure:

```plaintext
card-game-demo/
│
├── README.md                   # Project documentation
├── notebooks/                  # 📒 Jupyter Notebooks for experiments and analysis
│   ├── game_logic.ipynb        # Prototyping game logic
│   └── data_analysis.ipynb     # Exploring user data and insights
│
├── src/                        # 🧑‍💻 Core Python scripts
│   ├── card.py                 # Card class and deck logic
│   ├── game.py                 # Game mechanics and flow
│   └── utils.py                # Utility functions (e.g., for scoring)
│
├── tests/                      # 🧪 Automated tests
│   ├── test_card.py            # Tests for card functionalities
│   ├── test_game.py            # Tests for game logic and mechanics
│   └── test_utils.py           # Tests for utility functions
│
├── data/                       # 📊 Data storage
│   ├── game_logs.csv           # Logs of user actions and choices
│   └── analysis_results.csv    # Results from data analysis
│
└── dashboard/                  # 📊 Dynamic Dashboard (future milestone)
    ├── app.py                  # Python Dash app for visualizing the game state
    └── requirements.txt        # Dependencies for the dashboard
