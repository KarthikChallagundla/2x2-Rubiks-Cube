from pieces import Cube
import display_func as df

class Solver:
    def __init__(self, c):
        self.cube = c
        self.moves = []
        
    def move(self, move_str):
        self.moves.extend(move_str.split())
        self.cube.sequence(move_str)
    
    def undo(self, move_str):
        self.moves.pop()
        self.cube.sequence(move_str)
        
    def opp(self, color):
        if color == "R": return "O"
        elif color == "O": return "R"
        elif color == "B": return "G"
        elif color == "G": return "B"
        elif color == "W": return "Y"
        elif color == "Y": return "W"
        
    def solve(self):
        self.up_corners()
        self.oll()
        self.pll()
        while df.cube_str(self.cube.corners) != "WWWWGGRRBBOOGGRRBBOOYYYY":
            self.move("D")
        print(len(self.moves))
        print(self.moves)
        
        
    def up_corners(self):
        fru_piece = self.cube.find_piece(["R","B","W"])
        self.place_fru_corner(fru_piece)
        self.move("Z")
        bru_piece = self.cube.find_piece(["O","B","W"])
        self.place_fru_corner(bru_piece)
        self.move("Z")
        blu_piece = self.cube.find_piece(["O","G","W"])
        self.place_fru_corner(blu_piece)
        self.move("Z")
        flu_piece = self.cube.find_piece(["R","G","W"])
        self.place_fru_corner(flu_piece)
        self.move("Z")
        
    def place_fru_corner(self, corner_piece):
        if (corner_piece.position == [1,1,1]).all() and corner_piece.colors[2] == 'W':
            return
        if corner_piece.position[2] == 1:
            pos = [0,0,0]
            pos[1] = corner_piece.position[1]
            cw, cc = Cube.get_rot_from_face(pos)
            
            count = 0
            undo_move = cc
            while corner_piece.position[2] != -1:
                self.move(cw)
                count += 1
                
            if count > 1:
                for _ in range(count):
                    self.undo(cc)
                    
                count = 0
                while corner_piece.position[2] != -1:
                    self.move(cc)
                    count += 1
                undo_move = cw
            self.move("D")
            for _ in range(count):
                self.move(undo_move)
                
        while (corner_piece.position[0], corner_piece.position[1]) != (1,1):
            self.move("D")
            
        if corner_piece.colors[0] == "W":
            self.move("Di Ri D R")
        elif corner_piece.colors[1] == "W":
            self.move("D F Di Fi")
        elif corner_piece.colors[2] == "W":
            self.move("Ri D D R D D F Di Fi")
            
    def oll(self):
        self.move("Y Y")
        
        def state1():
            return (self.cube.get_piece(1,1,1).colors[0] == "Y" and
                    self.cube.get_piece(-1,1,1).colors[0] == "Y" and
                    self.cube.get_piece(-1,-1,1).colors[0] == "Y" and
                    self.cube.get_piece(1,-1,1).colors[0] == "Y")
        
        def state2():
            return (self.cube.get_piece(1,1,1).colors[0] == "Y" and
                    self.cube.get_piece(-1,1,1).colors[0] == "Y" and
                    self.cube.get_piece(-1,-1,1).colors[1] == "Y" and
                    self.cube.get_piece(1,-1,1).colors[1] == "Y")
            
        def state3():
            return (self.cube.get_piece(1,1,1).colors[0] == "Y" and
                    self.cube.get_piece(-1,1,1).colors[1] == "Y" and
                    self.cube.get_piece(-1,-1,1).colors[0] == "Y" and
                    self.cube.get_piece(1,-1,1).colors[2] == "Y")
            
        def state4():
            return (self.cube.get_piece(1,1,1).colors[1] == "Y" and
                    self.cube.get_piece(-1,1,1).colors[2] == "Y" and
                    self.cube.get_piece(-1,-1,1).colors[1] == "Y" and
                    self.cube.get_piece(1,-1,1).colors[0] == "Y")
            
        def state5():
            return (self.cube.get_piece(1,1,1).colors[2] == "Y" and
                    self.cube.get_piece(-1,1,1).colors[2] == "Y" and
                    self.cube.get_piece(-1,-1,1).colors[1] == "Y" and
                    self.cube.get_piece(1,-1,1).colors[1] == "Y")
            
        def state6():
            return (self.cube.get_piece(1,1,1).colors[2] == "Y" and
                    self.cube.get_piece(-1,1,1).colors[2] == "Y" and
                    self.cube.get_piece(-1,-1,1).colors[0] == "Y" and
                    self.cube.get_piece(1,-1,1).colors[0] == "Y")
            
        def state7():
            return (self.cube.get_piece(1,1,1).colors[2] == "Y" and
                    self.cube.get_piece(-1,1,1).colors[1] == "Y" and
                    self.cube.get_piece(-1,-1,1).colors[2] == "Y" and
                    self.cube.get_piece(1,-1,1).colors[0] == "Y")
            
        def state8():
            return (self.cube.get_piece(1,1,1).colors[2] == "Y" and
                    self.cube.get_piece(-1,1,1).colors[2] == "Y" and
                    self.cube.get_piece(-1,-1,1).colors[2] == "Y" and
                    self.cube.get_piece(1,-1,1).colors[2] == "Y")
            
        while not state8():
            if state1():
                self.move("R R U U R U U R R")
            elif state2():
                self.move("F R U Ri Ui R U Ri Ui Fi")
            elif state3():
                self.move("R U Ri U R U U Ri")
            elif state4():
                self.move("R U U Ri Ui R Ui Ri")
            elif state5():
                self.move("F R U Ri Ui Fi")
            elif state6():
                self.move("R U Ri Ui Ri F R Fi")
            elif state7():
                self.move("F R Ui Ri Ui R U Ri Fi")
            else:
                self.move("U")
                
    def pll(self):
        def state1():
            return (self.opp(self.cube.get_piece(1,-1,1).colors[0]) == self.cube.get_piece(-1,1,1).colors[0] and
                    self.opp(self.cube.get_piece(1,-1,1).colors[1]) == self.cube.get_piece(-1,1,1).colors[1])
            
        def state2():
            return (self.cube.get_piece(1,-1,1).colors[1] == self.cube.get_piece(-1,-1,1).colors[1] and
                    self.cube.get_piece(1,1,1).colors[1] != self.cube.get_piece(-1,1,1).colors[1])
            
        def state3():
            return (self.cube.get_piece(1,-1,1).colors[1] == self.cube.get_piece(-1,-1,1).colors[1] and
                    self.cube.get_piece(1,1,1).colors[1] == self.cube.get_piece(-1,1,1).colors[1])
            
        while not state3():
            if state1():
                self.move("F R Ui Ri Ui R U Ri Fi R U Ri Ui Ri F R Fi")
            elif state2():
                self.move("R U Ri Ui Ri F R R Ui Ri Ui R U Ri Fi")
            else:
                self.move("U")
                
        self.move("Y Y")