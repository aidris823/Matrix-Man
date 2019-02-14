"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    '''example matrix:
Input:
    [[1,2,3,1][4,5,6,1][5,10,12,1]]=
Output:
[
1 4 5 
2 5 10
3 6 12
1 1 1
]
'''
    print '[\n'
    col1 = ''
    col2 = ''
    col3 = ''
    col4 = ''
    for i in range(len(matrix)):
        col1 += str(matrix[i][0]) + " "
    print col1 + '\n' 
    for i in range(len(matrix)):
        col2 += str(matrix[i][1]) + " "
    print col2 + '\n'
    for i in range(len(matrix)):
        col3 += str(matrix[i][2]) + " " 
    print col3 + '\n'
    for i in range(len(matrix)):
        col4 += str(matrix[i][3]) + " " 
    print col4 + '\n]'
example_matrix = [[1,2,3,1],[4,5,6,1],[5,10,12,1]]
print_matrix(example_matrix)

x = list([[],[],[],[],[],[]])
x[4] = "hello"
print x



#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    pass

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    '''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    Ex: [[
    '''
    rows = len(m1)
    cols = len(m2[0])

    if (len(m1[0]) != len(m2)):
        print "Invalid multiplication"
        return
    i = 0
    ans = list()
    for i in range(rows):
        
    




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
