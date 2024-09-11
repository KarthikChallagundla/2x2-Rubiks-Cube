# 2x2 Rubik's Cube Simulator and Solver

This project is a Python and NumPy-based 2x2 Rubik's Cube simulator and solver. It enables users to simulate the cube, perform various moves, scramble it, and compute the optimal solution for any scrambled configuration.

## ScreenShots
### Initial Cube State
![Initial Cube State](static/screenshot/initial_cube.png?raw=true)
### Scrambled Cube
![Scrambled Cube](static/screenshot/scrambled_cube.png?raw=true)
### Solution Steps
![Solution Steps](static/screenshot/solution_steps.png?raw=true)
### Solved Cube
![Solved Cube](static/screenshot/solved_cube.png?raw=true)

## Features

- Simulate a 2x2 Rubik's Cube with all standard moves (rotations of any face).
- Display the cube's current state before and after each move.
- Supports user input for manual cube rotations.

## Technologies Used

- Python
- NumPy

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/KarthikChallagundla/2x2-Rubiks-Cube.git
    ```

2. Navigate to the project directory:

    ```
    cd 2x2-Rubiks-Cube
    ```

3. Install dependencies:

    ```
    pip install requirements.txt
    ```

4. Run the simulation:

    ```
    python cube.py
    ```

## Usage

- Run the simulation script using the command mentioned above.
- The program provides the following features:
  - **Solve**: Automatically solves the cube using the least number of moves.
  - **Rotate**: Allows you to manually rotate any face of the cube.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by the challenge of solving the 2x2 Rubik's Cube using Python.
- Special thanks to the NumPy community for providing an efficient numerical computing library.
