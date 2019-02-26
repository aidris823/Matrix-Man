from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 255, 0 ]
matrix = new_matrix()

add_edge(matrix,50,50,0,100,100,0)
add_edge(matrix,100,100,0,200,250,0)
add_edge(matrix,200,250,0,50,50,0)

square_matrix = [[99,99,99,99],[99,99,99,99],[99,99,99,99],[99,99,99,99]]
print_matrix(square_matrix)
print("\n Testing ident function:")
print_matrix(ident(square_matrix))

print("Testing matrix multiplication")
m1 = [[1,2,3,0],[4,5,6,0],[10,11,12,13],[12,12,144,15]]
m2 = [[7,2,5,9],[10,12,15,11],[64,65,21,25],[21,22,23,24]]
print_matrix(m1)
print_matrix(m2)
print("m1*m2 = \n")
matrix_mult(m1,m2)
print_matrix(m2)

draw_lines( matrix, screen, color )
display(screen)


