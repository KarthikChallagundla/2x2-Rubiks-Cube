import numpy as np
from termcolor import colored

front_face = ['0','0','0','0']
right_face = ['0','0','0','0']
up_face = ['0','0','0','0']
back_face = ['0','0','0','0']
left_face = ['0','0','0','0']
down_face = ['0','0','0','0']

def equal_pos(pos1, pos2):
    if (np.array(pos1) == np.array(pos2)).all():
        return True
    return False

def color_piece(i):
    fore_color = ''
    back_color = ''
    if i == 'W':
        fore_color = 'white'
        back_color = 'on_white'
    elif i=='Y':
        fore_color = 'yellow'
        back_color = 'on_yellow'
    elif i=='R':
        fore_color = 'red'
        back_color = 'on_red'
    elif i=='O':
        fore_color = 'light_red'
        back_color = 'on_light_red'
    elif i=='B':
        fore_color = 'blue'
        back_color = 'on_blue'
    elif i=='G':
        fore_color = 'green'
        back_color = 'on_green'
            
    return colored('  ', fore_color, back_color)

def print_list_as_color(list):
    fore_color = []
    back_color = []
    for i in list:
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
        

def display_front_face(list):
    print("Front face : ")
    for i in list:
        if equal_pos(i.position, [1,-1,1]):     front_face[0] = i.colors[0]
        elif equal_pos(i.position, [1,1,1]):    front_face[1] = i.colors[0]
        elif equal_pos(i.position, [1,-1,-1]):  front_face[2] = i.colors[0]
        elif equal_pos(i.position, [1,1,-1]):   front_face[3] = i.colors[0]
    print_list_as_color(front_face)
    
def display_right_face(list):
    print("Right face : ")
    for i in list:
        if equal_pos(i.position, [1,1,1]):      right_face[0] = i.colors[1]
        elif equal_pos(i.position, [-1,1,1]):   right_face[1] = i.colors[1]
        elif equal_pos(i.position, [1,1,-1]):   right_face[2] = i.colors[1]
        elif equal_pos(i.position, [-1,1,-1]):  right_face[3] = i.colors[1]
    print_list_as_color(right_face)
    
def display_up_face(list):
    print("Top face : ")
    for i in list:
        if equal_pos(i.position, [-1,-1,1]):    up_face[0] = i.colors[2]
        elif equal_pos(i.position, [-1,1,1]):   up_face[1] = i.colors[2]
        elif equal_pos(i.position, [1,-1,1]):   up_face[2] = i.colors[2]
        elif equal_pos(i.position, [1,1,1]):    up_face[3] = i.colors[2]
    print_list_as_color(up_face)
    
def display_back_face(list):
    print("Back face : ")
    for i in list:
        if equal_pos(i.position, [-1,1,1]):     back_face[0] = i.colors[0]
        elif equal_pos(i.position, [-1,-1,1]):  back_face[1] = i.colors[0]
        elif equal_pos(i.position, [-1,1,-1]):  back_face[2] = i.colors[0]
        elif equal_pos(i.position, [-1,-1,-1]): back_face[3] = i.colors[0]
    print_list_as_color(back_face)
    
def display_left_face(list):
    print("Left face : ")
    for i in list:
        if equal_pos(i.position, [-1,-1,1]):     left_face[0] = i.colors[1]
        elif equal_pos(i.position, [1,-1,1]):    left_face[1] = i.colors[1]
        elif equal_pos(i.position, [-1,-1,-1]):  left_face[2] = i.colors[1]
        elif equal_pos(i.position, [1,-1,-1]):   left_face[3] = i.colors[1]
    print_list_as_color(left_face)
    
def display_down_face(list):
    print("Bottom face : ")
    for i in list:
        if equal_pos(i.position, [1,-1,-1]):     down_face[0] = i.colors[2]
        elif equal_pos(i.position, [1,1,-1]):    down_face[1] = i.colors[2]
        elif equal_pos(i.position, [-1,-1,-1]):  down_face[2] = i.colors[2]
        elif equal_pos(i.position, [-1,1,-1]):   down_face[3] = i.colors[2]
    print_list_as_color(down_face)
    
def display_all_faces(list):
    display_front_face(list)
    display_right_face(list)
    display_up_face(list)
    display_back_face(list)
    display_left_face(list)
    display_down_face(list)
    
def display_cube(list):
    print(f"      {color_piece(up_face[0])} {color_piece(up_face[1])}            ", end='\n\n')
    print(f"      {color_piece(up_face[2])} {color_piece(up_face[3])}            ", end='\n\n')
    print(f"{color_piece(left_face[0])} {color_piece(left_face[1])} {color_piece(front_face[0])} {color_piece(front_face[1])} {color_piece(right_face[0])} {color_piece(right_face[1])} {color_piece(back_face[0])} {color_piece(back_face[1])}", end='\n\n')
    print(f"{color_piece(left_face[2])} {color_piece(left_face[3])} {color_piece(front_face[2])} {color_piece(front_face[3])} {color_piece(right_face[2])} {color_piece(right_face[3])} {color_piece(back_face[2])} {color_piece(back_face[3])}", end='\n\n')
    print(f"      {color_piece(down_face[0])} {color_piece(down_face[1])}            ", end='\n\n')
    print(f"      {color_piece(down_face[2])} {color_piece(down_face[3])}            ", end='\n\n')
    
def cube_str(list):
    return "".join(up_face + left_face[:2] + front_face[:2] + right_face[:2] + back_face[:2] + left_face[2:] + front_face[2:] + right_face[2:] + back_face[2:] + down_face)