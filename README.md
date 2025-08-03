# Python Pong Game

A classic two-player Pong game implementation using Python's Turtle graphics module. This recreation features smooth paddle movement, score tracking, and a pause function.

## Features

- Two-player gameplay
- Real-time score tracking
- Pause functionality (Space bar)
- Center line visualization
- Paddle and ball collision detection
- Smooth animations
- Classic retro styling

## Controls

- **Right Paddle:** 
  - Up Arrow: Move Up
  - Down Arrow: Move Down

- **Left Paddle:**
  - W: Move Up
  - S: Move Down

- **Game Control:**
  - Space Bar: Pause/Unpause

## Requirements

- Python 3.x
- Python's built-in Turtle graphics module

## Project Structure

```
pong_game/
│
├── main.py         # Game loop and main functionality
├── paddle.py       # Paddle class definition
├── ball.py         # Ball class definition
└── scoreboard.py   # Scoreboard class definition
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pong_game.git
cd pong_game
```

2. Run the game:
```bash
python main.py
```

## Game Rules

- Each player controls a paddle on their side of the screen
- The ball bounces off paddles and walls
- Missing the ball gives the opponent a point
- The game continues indefinitely - play until you decide to stop!

## Contributing

Feel free to fork the project and submit pull requests for any improvements you'd like to add!

## License

This project is open source and available under the MIT License.
