# 2x2 Rubik's Cube Simulator and Solver

This project is a Python and NumPy-based 2x2 Rubik's Cube simulator and solver. It enables users to simulate the cube, perform various moves, scramble it, and compute the optimal solution for any scrambled configuration. Additionally, it includes a graphical user interface (GUI) for visualizing the cube and interacting with it in real-time.

## Features

- Simulate a 2x2 Rubik's Cube with all standard moves (rotations of any face).
- Display the cube's current state before and after each move.
- Supports user input for manual cube rotations.
- **Graphical User Interface (GUI)**: A simple GUI to visualize the 2x2 Rubik's Cube, where users can interact with the cube using buttons and keyboard controls.
  - Rotate the cube faces using GUI buttons or keyboard keys.
  - View the cube’s state graphically as you make moves.
  - Perform any of the 6 basic moves (R, L, U, D, F, B) and their inverse counterparts.
  
## Technologies Used

- Python
- NumPy
- Tkinter (for GUI)

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
    pip install -r requirements.txt
    ```

4. Run the simulation script:

    ```
    python cube.py
    ```

5. To run visualization using tkinter, run the following script:

    ```
    python gui_2d.py
    ```

6. To use the GUI:

    - Run any one of the file from `cube.py` or `gui_2d.py` to see the simulation
    - Running `gui_2d.py` will launch the Tkinter-based GUI window where you can visualize the cube and interact with it.

## Usage

- Run the simulation script using the command mentioned above.
- The program provides the following features:
  - **Solve**: Automatically solves the cube using the least number of moves.
  - **Rotate**: Allows you to manually rotate any face of the cube.
  - **GUI Controls**: Use the provided GUI to rotate the cube’s faces either by clicking buttons or using the keyboard. The supported key controls are:
    - `r` for rotating the right face clockwise.
    - `R` for rotating the right face counter-clockwise.
    - `l` for rotating the left face clockwise.
    - `L` for rotating the left face counter-clockwise.
    - `u` for rotating the upper face clockwise.
    - `U` for rotating the upper face counter-clockwise.
    - `d` for rotating the down face clockwise.
    - `D` for rotating the down face counter-clockwise.
    - `f` for rotating the front face clockwise.
    - `F` for rotating the front face counter-clockwise.
    - `b` for rotating the back face clockwise.
    - `B` for rotating the back face counter-clockwise.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by the challenge of solving the 2x2 Rubik's Cube using Python.
- Special thanks to the NumPy community for providing an efficient numerical computing library.
- Thanks to Tkinter for providing a simple and effective way to create the graphical user interface.
