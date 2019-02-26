from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 255, 0 ]
matrix = new_matrix()

add_edge(matrix,50,50,0,100,100,0)
add_edge(matrix,100,100,0,200,250,0)
add_edge(matrix,200,250,0,50,50,0)

draw_lines( matrix, screen, color )
display(screen)
