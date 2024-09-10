import numpy as np
import display_func as df
from termcolor import colored

# Matrices for rotating the cube
rl_dash = np.array([[0,0,-1],[0,1,0],[1,0,0]])
lr_dash = np.array([[0,0,1],[0,1,0],[-1,0,0]])
ud_dash = np.array([[0,1,0],[-1,0,0],[0,0,1]])
du_dash = np.array([[0,-1,0],[1,0,0],[0,0,1]])
fb_dash = np.array([[1,0,0],[0,0,1],[0,-1,0]])
bf_dash = np.array([[1,0,0],[0,0,-1],[0,1,0]])

# Here is the definitions of faces
FRONT = X_AXIS = np.array([1,0,0])
BACK = np.array([-1,0,0])
RIGHT = Y_AXIS = np.array([0,1,0])
LEFT = np.array([0,-1,0])
UP = Z_AXIS = np.array([0,0,1])
DOWN = np.array([0,0,-1])

# print_as_color function used to print pieces as colors
def print_as_color(color):
    if i == 'W':
        fore_color.append('white')
        back_color.append('on_white')
    elif i=='Y':
        fore_color.append('yellow')
        back_color.append('on_yellow')
    elif i=='R':
        fore_color.append('red')
        back_color.append('on_red')
    elif i=='O':
        fore_color.append('light_red')
        back_color.append('on_light_red')
    elif i=='B':
        fore_color.append('blue')
        back_color.append('on_blue')
    elif i=='G':
        fore_color.append('green')
        back_color.append('on_green')
            
    list = np.array(list).reshape(2,2)
    fore_color = np.array(fore_color).reshape(2,2)
    back_color = np.array(back_color).reshape(2,2)
    
    for i in range(len(list)):
        for j in range(len(list[i])):
            print(colored('  ', fore_color[i][j], back_color[i][j]), end=' ')
        print('\n')

# Class Piece defines the pieces of cube
class Piece:
    def __init__(self, pos, colors):        
        self.position = np.array(pos)
        self.colors = np.array(colors)
        self.orientation = np.array([2,3,4]) * self.position
        self.join = dict(zip(colors, self.orientation))
    
    def rejoin(self):
        self.join = dict(zip(self.colors, self.orientation))
        
# Cube defines the entire 2*2 rubiks cube
class Cube:
    def __init__(self, str):
        self.corners = (
            Piece([1,1,1], [str[7],str[8],str[3]]),
            Piece([1,1,-1], [str[15],str[16],str[21]]),
            Piece([1,-1,1], [str[6],str[5],str[2]]),
            Piece([1,-1,-1], [str[14],str[13],str[20]]),
            Piece([-1,1,1], [str[10],str[9],str[1]]),
            Piece([-1,1,-1], [str[18],str[17],str[23]]),
            Piece([-1,-1,1], [str[11],str[4],str[0]]),
            Piece([-1,-1,-1], [str[19],str[12],str[22]]),
        )
        
    def _face(self, axis):
        return [p for p in self.corners if p.position.dot(axis) > 0]
    
    def find_piece(self, colors):
        for p in self.corners:
            if all(c in p.colors for c in colors):
                return p
    
    def get_piece(self, x, y, z):
        for p in self.corners:
            if (p.position == np.array([x,y,z])).all():
                return p
            
    def cube_str(self):
        a = self.get_piece(-1,-1,1).colors
        b = self.get_piece(-1,1,1).colors
        c = self.get_piece(1,-1,1).colors
        d = self.get_piece(1,1,1).colors
        e = self.get_piece(-1,-1,-1).colors
        f = self.get_piece(-1,1,-1).colors
        g = self.get_piece(1,-1,-1).colors
        h = self.get_piece(1,1,-1).colors
        
        str = f"{a[2]}{b[2]}{c[2]}{d[2]}{a[1]}{c[1]}{c[0]}{d[0]}{d[1]}{b[1]}{b[0]}{a[0]}{e[1]}{g[1]}{g[0]}{h[0]}{h[1]}{f[1]}{f[0]}{e[0]}{e[2]}{f[2]}{g[2]}{h[2]}"
        return str
            
    def get_rot_from_face(face):
        if (face == FRONT).all() : return "F","Fi"
        elif (face == RIGHT).all() : return "R","Ri"
        elif (face == UP).all() : return "U","Ui"
        elif (face == BACK).all() : return "B","Bi"
        elif (face == LEFT).all() : return "L","Li"
        elif (face == DOWN).all() : return "D","Di"
        
    def rotate_face(self, face, mat, inv):
        for i in self._face(face):
            changed = []
            i.position = np.dot(mat,i.position)
            for j in range(len(i.orientation)):
                if i.orientation[j] < 0:
                    changed.append(j)
                    i.orientation[j] = abs(i.orientation[j])
            i.orientation = np.dot(inv,i.orientation)
            if len(changed) != 0:
                for j in changed:
                    i.orientation[j] = i.orientation[j]*-1
            i.rejoin()
            i.orientation = sorted(i.orientation, key=abs)
            i.join = sorted(i.join.items(), key=lambda x:abs(x[1]))
            i.colors = []
            for j in i.join:
                i.colors.append(j[0])
            
    def R(self): self.rotate_face(RIGHT, rl_dash, lr_dash)
    def Ri(self): self.rotate_face(RIGHT, lr_dash, rl_dash)
    def L(self): self.rotate_face(LEFT, lr_dash, rl_dash)
    def Li(self): self.rotate_face(LEFT, rl_dash, lr_dash)
    def U(self): self.rotate_face(UP, ud_dash, du_dash)
    def Ui(self): self.rotate_face(UP, du_dash, ud_dash)
    def D(self): self.rotate_face(DOWN, du_dash, ud_dash)
    def Di(self): self.rotate_face(DOWN, ud_dash, du_dash)
    def F(self): self.rotate_face(FRONT, fb_dash, bf_dash)
    def Fi(self): self.rotate_face(FRONT, bf_dash, fb_dash)
    def B(self): self.rotate_face(BACK, bf_dash, fb_dash)
    def Bi(self): self.rotate_face(BACK, fb_dash, bf_dash)
    
    def R2(self): self.R(), self.R()
    def L2(self): self.L(), self.L()
    def U2(self): self.U(), self.U()
    def D2(self): self.D(), self.D()
    def F2(self): self.F(), self.F()
    def B2(self): self.B(), self.B()
    
    def X(self): self.F(), self.Bi()
    def Xi(self): self.Fi(), self.B()
    def Y(self): self.R(), self.Li()
    def Yi(self): self.Ri(), self.L()
    def Z(self): self.U(), self.Di()
    def Zi(self): self.Ui(), self.D()
    
    def sequence(self, move_str):
        moves = [getattr(self, name) for name in move_str.split()]
        for move in moves:
            move()
            
    def display_cube(self):
        df.display_all_faces(self.corners)
        
    def is_solved(self):
        str = self.cube_str()
        return (str[0] == str[1] and str[1] == str[2] and str[2] == str[3] and
                str[4] == str[5] and str[5] == str[12] and str[12] == str[13] and
                str[6] == str[7] and str[7] == str[14] and str[14] == str[15] and
                str[8] == str[9] and str[9] == str[16] and str[16] == str[17] and
                str[10] == str[11] and str[11] == str[18] and str[18] == str[19] and
                str[20] == str[21] and str[21] == str[22] and str[22] == str[23])
    
    