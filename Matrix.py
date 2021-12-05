import random
import numpy as np
class bcolors:
    HEADER = '\033[95m'
    ENDC = '\033[0m'


#ARRAYS
print(bcolors.HEADER + "ARRAYS" + bcolors.ENDC)
num_rows = 4
num_columns = 4
random.seed(0)
A = np.array([[random.randint(0, 10) for j in range(num_rows)] for i in range(num_columns)])
print("Matrix A is =\n", A)

B = np.identity(4)
print ("Matrix B is =\n" , B) 
print("\n")

#A --- Function -- Sum of A and B matrices
print(bcolors.HEADER + "Function -- Sum of A and B matrices" + bcolors.ENDC)
add = np.add(A, B) 
print ("Sum of A and B =\n", add) 


#B ---- Sum of all numbers in Both matrices
#Sum of all numbers in A matrix
sum = np.sum([A])
print ("Sum of all numbers in A matrix =", sum)
#Sum of all numbers in B matrix
sum = np.sum([B])
print ("Sum of all numbers in B identity matrix =", sum)
#Sum of all numbers in Both matrices
sum = np.sum([A, B])
print ("Sum of all numbers in both matrices =", sum)


#C ---- Find the maximum value in A matrix
print("\n")
print(bcolors.HEADER + "Find the maximum value in A matrix" + bcolors.ENDC)
max = np.amax(A)
print('The maximum value in A matrix is = ', max)


#D ---- Reshape A to have 8 rows and B to have 8 columns and then multiply them. 
print("\n")
print(bcolors.HEADER + "Reshape A to have 8 rows and B to have 8 columns and then multiply them." + bcolors.ENDC)
reshapedA = A.reshape(8, 2)
print("Reshaped A with 8 rows =\n", reshapedA)
reshapedB = B.reshape(2, 8)
print("Reshaped B with 8 columns =\n", reshapedB)

#Multiplication of reshapedA and reshapedB
mul = np.dot(reshapedA, reshapedB)
print("Multiply of reshapedA and ReshapedB is =\n", mul)


#E ---- Find the sum of values from the third column in A and third row in B
#[0, 6, 9, 4] = 19     +    [0, 0, 1, 0]=1.0    =   20.0
print("\n")
print(bcolors.HEADER + "Find the sum of values from the third column in A and third row in B" + bcolors.ENDC)
x = A[:, 2:3]
y = B[2:3, :]
xd = np.sum([x])
xy = np.sum([y])
print("Sum of the values from third column in A and third row in B =\n", xd , xy)
sum = np.sum([xd, xy])
print("Sum of the values from third column in A and third row in B =\n", sum)


#F ---- For every value in second column swap it with this value squared ()
print("\n")
print(bcolors.HEADER + "For every value in second column swap it with this value squared" + bcolors.ENDC)
sqA = np.square(A[:, 1:2])
sqB = np.square(B[:, 1:2])
print("Squared second column of A =\n",sqA)
print("Squared second column of B =\n",sqB)

A[:, 1:2] = np.square(A[:, 1:2])
B[:, 1:2] = np.square(B[:, 1:2])

print("\n After swapping arrays:")
print("After swapping A matrix =\n", A)
print("\n")
print("After swapping B matrix =\n",B)

#G ---- Join A and B horizontally (so new matrix has 8 columns and 4 rows)
print("\n")
print(bcolors.HEADER + "Join A and B horizontally" + bcolors.ENDC)
join = np.hstack((A,B))
print("Joined A and B horizontally:\n", join)


#H ---- Change the type of the arrays A and B in that way, that they contain strings. Then add them (A+B)
print("\n")
print(bcolors.HEADER + "Change the type of the arrays A and B in that way, that they contain strings. Then add them (A+B)" + bcolors.ENDC)

Astr = np.array(A, dtype = str)
Bstr = np.array(B, dtype = str)
print("Changed result is: \n" + str(np.core.defchararray.add(Astr,Bstr)))



#3 CALCULATING OF EXPRESSION 
#A ARRAY
A = np.array([[3, 4, 5],[6, 7, 8],[9, 10, 11,]])
print("A array = \n", A)

print("\n")
#B ARRAY
B = np.array([[2, 2, 2],[2, 2, 2,]])
print("B array = \n", B)




print("\n")
#TRANSPOSE
T = np.transpose(A)
print("Transposed A = \n", T)

#  IT WAS NOT POSSIBLE TO DO THE EXPRESSION #
# The number of columns of the first matrix is equal to the number of rows of the second matrix.
# And I changed the positions as B x A(transpose) instead of A(transpose) x B

print("\n")
mul = np.dot(B, T)
print("Multiplied B array and Transposed A array is =\n", mul)

# Or Transpose and Mul at the same time
print("Multiplied B array and Transposed A array is = \n" + str(B @ np.transpose(A)))