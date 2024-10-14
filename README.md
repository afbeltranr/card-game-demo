# 🃏 Card Game Demo Project

Welcome to the **Card Game Demo** project! This project aims to build a simple yet engaging card game using Python. The focus is on creating a text-based game that can later be expanded with a dynamic dashboard for visualizations and potentially multiplayer functionality. 

## 🎯 Project Overview
In this card game, players draw from either a **pile of unknown cards** or a **pile of known discarded cards**. The goal is to **achieve the lowest score** based on the values of cards in hand, with special scoring rules for certain cards:

- Red King ♔ = 0 points
- Black King ♚ = 20 points
- Other cards = their face value (e.g., 2-10, J, Q)

The game includes a special rule for **cutting turns**, where a player can interrupt the next player if they have a matching card.

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
- Plan data storage and analysis methods (e.g., using pandas for tracking).

### 3. 🛠️ Construct
- Build the core game components:
  - **Card Class**: Represents a card with its number, suit, and color.
  - **Deck Class**: Manages the deck, draw pile, and discard pile.
  - **Game Logic**: Implements player turns, drawing, discarding, and scoring.
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
