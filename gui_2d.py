import tkinter as tk
from tkinter import Canvas
import numpy as np
from pieces import Cube
from solve import Solver

class CubeGUI:
    def __init__(self, cube):
        self.cube = cube
        self.colors = {
            'W': 'white',
            'Y': 'yellow',
            'R': 'red',
            'O': 'orange',
            'B': 'blue',
            'G': 'green'
        }
        self.window = tk.Tk()
        self.window.title("2x2 Rubik's Cube")
        self.canvas = Canvas(self.window, width=600, height=400, bg="black")
        frame = tk.Frame(self.window)
        frame.pack(pady=10)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.moves_text = tk.Text(frame, height=3, width=70, yscrollcommand=scrollbar.set)
        self.moves_text.pack(side=tk.LEFT)

        scrollbar.config(command=self.moves_text.yview)
        self.canvas.pack()
        self.draw_cube()

        # Binding keyboard events for cube moves
        self.window.bind("<r>", lambda event: self.apply_move("R"))
        self.window.bind("<R>", lambda event: self.apply_move("Ri"))
        self.window.bind("<l>", lambda event: self.apply_move("L"))
        self.window.bind("<L>", lambda event: self.apply_move("Li"))
        self.window.bind("<u>", lambda event: self.apply_move("U"))
        self.window.bind("<U>", lambda event: self.apply_move("Ui"))
        self.window.bind("<d>", lambda event: self.apply_move("D"))
        self.window.bind("<D>", lambda event: self.apply_move("Di"))
        self.window.bind("<f>", lambda event: self.apply_move("F"))
        self.window.bind("<F>", lambda event: self.apply_move("Fi"))
        self.window.bind("<b>", lambda event: self.apply_move("B"))
        self.window.bind("<B>", lambda event: self.apply_move("Bi"))

    def draw_face(self, x, y, face_colors):
        size = 50
        for i in range(2):
            for j in range(2):
                color = self.colors[face_colors[i * 2 + j]]
                self.canvas.create_rectangle(
                    x + j * size, y + i * size,
                    x + (j + 1) * size, y + (i + 1) * size,
                    fill=color, outline="black"
                )

    def draw_cube(self):
        cube_str = self.cube.cube_str()
        faces = {
            'U': cube_str[0:4],
            'R': cube_str[8:10] + cube_str[16:18],
            'F': cube_str[6:8] + cube_str[14:16],
            'D': cube_str[20:],
            'L': cube_str[4:6] + cube_str[12:14],
            'B': cube_str[10:12] + cube_str[18:20]
        }

        # Position faces relative to each other
        self.draw_face(150, 50, faces['U'])  # Up
        self.draw_face(250, 150, faces['R'])  # Right
        self.draw_face(150, 150, faces['F'])  # Front
        self.draw_face(50, 150, faces['L'])  # Left
        self.draw_face(150, 250, faces['D'])  # Down
        self.draw_face(350, 150, faces['B'])  # Back

    def apply_move(self, move):
        getattr(self.cube, move)()
        self.canvas.delete("all")
        self.draw_cube()

    def solve_cube(self):
        cube_str = self.cube.cube_str()
        temp_cube = Cube(cube_str)
        solver = Solver(temp_cube)
        solver.solve()

        self.solution_moves = solver.moves

        self.moves_text.delete("1.0", tk.END)
        self.moves_text.insert(tk.END, " ".join(self.solution_moves))

    def run(self):
        control_frame = tk.Frame(self.window)
        control_frame.pack()

        moves = ["R", "Ri", "L", "Li", "U", "Ui", "D", "Di", "F", "Fi", "B", "Bi"]

        for move in moves:
            button = tk.Button(control_frame, text=move, command=lambda m=move: self.apply_move(m))
            button.pack(side="left")

        solve_btn = tk.Button(control_frame, text="Solve Cube", command=self.solve_cube)
        solve_btn.pack(side="left")

        self.window.mainloop()

# Example usage:
if __name__ == "__main__":
    cube = Cube("WWWWGGRRBBOOGGRRBBOOYYYY")  # Example solved cube string
    gui = CubeGUI(cube)
    gui.run()
