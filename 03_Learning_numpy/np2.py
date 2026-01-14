# Array indexing
# forward  indexing: 0  1  2  3  4
#             value: 5  1  3  2  7
# backword indexing:-5 -4 -3 -2 -1

import numpy as np

ar = np.arange(1,8)
print(ar)
print(ar[1:3:1])
print(ar[0:5:2])
print(ar[-1:-8:-1])

print("\n======================")
arr = np.arange(1,10).reshape(3,3)
print(arr)
print()

print(arr[1][1])
print(arr[1,1]) # both way are correct but we use this one
print(arr[0,:]) # printing 1st row
print()
print(arr[:,2]) # printing 3rd colum
print()
print(arr[0:2,1:3])