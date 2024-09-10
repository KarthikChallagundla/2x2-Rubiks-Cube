from pieces import Cube
from solve import Solver
import display_func as df


# Cube string format

#       00 01
#       02 03
# 04 05 06 07 08 09 10 11
# 12 13 14 15 16 17 18 19
#       20 21
#       22 23

cube = Cube("WWWWGGRRBBOOGGRRBBOOYYYY") # Add the cube string here

print("The preview of the cube is ")
cube.display_cube()

moves_names = ['R','Ri','L','Li','U','Ui','D','Di','F','Fi','B','Bi']

while True:
    
    print("-----Main Menu-----")
    
    print("1.R 2.R\'")
    print("3.L 4.L\'")
    print("5.U 6.U\'")
    print("7.D 8.D\'")
    print("9.F 10.F\'")
    print("11.B 12.B\'")
    print("13. Display all the faces")
    print("14. Display whole cube")
    print("15. Solve the cube")
    print("16. EXIT")
    opt = int(input("Choose an option : "))
    if opt <= 12 :
        cube.sequence(moves_names[opt - 1])
        print(f"{moves_names[opt-1]} is performed")
    elif opt == 13:
        df.display_all_faces(cube.corners)
    elif opt == 14:
        df.display_cube(cube.corners)
    elif opt == 15:
        solution = Solver(cube)
        solution.solve()
    elif opt == 16:
        break