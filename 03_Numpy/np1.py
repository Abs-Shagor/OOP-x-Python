import numpy as np

# creating 1d array. ex
arr1 = [2,1,4,3,5]

arr1 = np.array(arr1)
print(arr1)
print("----")
for i in range(0,5,1):
    print(arr1[i],end=" ")
print("\n----")
for i in range(4,-1,-1):
    print(arr1[i],end=" ")
print("\n----")


# creating 2d array. ex
arr2 = [[2,1,3],[8,1,7],[1,2,1]]
arr2 = np.array(arr2)
print(arr2)
print()

# we can also create an array by using arange. ex
arr3 = np.arange(1,7) #it's create an array which contain element from 1 to 6
print(arr3)
print()

# we can also create a 2d array by reshaping. ex
arr4 = np.arange(1,10).reshape(3,3)
print(arr4)
print()

arr5 = np.ones(5) # also can create for zeros
print(arr5)
print()
arr6 = np.ones((2,3))
print(arr6)

