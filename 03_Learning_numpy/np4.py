# some basic function
import numpy as np

mat = [[2,1,2],[1,1,1],[3,2,4]]
mat = np.array(mat)
print(mat)

print("----------")

# rowwise sorting
mat = np.sort(mat,axis=1)
print(mat)

print("----------")

# columwise sorting
mat = np.sort(mat,axis=0)
print(mat)

print(np.max(mat))
print(np.min(mat))
print(np.sum(mat))
print(np.prod(mat))
print(np.mean(mat)) # mean or average = sum/number of element
print(np.median(mat))
print(np.std(mat)) # standard deviation(there is a formula of it,check it in google)
print(np.var(mat)) # variance