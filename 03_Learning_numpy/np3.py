# Arithmatic operation
# addition(+),subtraction(-)
# multiplication(*),matrix multiplication(@)
# Division(/),floor Division(//)
# Exponentiation(**),modulo(%),transpose
import numpy as np

mat1 = [[2,1,2],[1,1,1],[3,2,4]]
mat2 = [[1,3,2],[2,1,3],[1,2,3]]
mat1 = np.array(mat1)
mat2 = np.array(mat2)
print(mat1)
print("------------------")
print(mat2)
print("------------------")

ans = mat1+mat2 # just change the sign 
print(ans)

print("------------------")
ansx = np.dot(mat1,mat2) # both matrix multiplication and dot product behave same 
print(ansx)              # for 2d matrix but are differ in higher dimenion
print("------------------")
print(mat1.transpose()) # transpose mean row will become colum and c. will become row

