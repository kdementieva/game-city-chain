# Game "Cities"

This project implements a console-based game called "Cities" in Python. The game is based on the rules where each player must name a city that starts with the last letter of the city named by the previous player. If a player cannot name a suitable city, the game ends.

## Description

### Main Files

- `cities.txt` - a text file containing a list of cities. It is used by the program to pick random cities.
- `answers.txt` - a file that records cities already used in the game to avoid repetition.

### Game Logic

1. The computer randomly selects a city from the `cities.txt` list.
2. The player enters a city that should start with the last letter of the previous city.
3. If the city has already been used, does not exist, or does not follow the rules, the player gets another attempt.
4. The game ends if:
   - The player runs out of attempts (5 errors).
   - The computer cannot find a suitable city.

### Main Functions

- **`get_city(letter='')`** — selects a random city from the `cities.txt` list. If a letter is provided, it searches for a city starting with that letter.
- **`check_city(user_city, opponent_city)`** — checks if the city entered by the user exists, has not already been used, and starts with the correct letter.

### Win and Loss Conditions

- Win: The computer cannot find a suitable city to respond with.
- Loss: The player makes 5 consecutive mistakes.

### Saving Results

The game saves all used cities in the `answers.txt` file, which can be used for analysis or checking for repeated cities.