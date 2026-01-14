# We can initialize data types directly like: st = “shagor” | x = 56 | y = 3.82
# or we can use type annotations like:  a:int=20 | st:str = "shagor bhai"

# List: a = [56, 'c', 3.82, 'shagor']   ==>List: support all datatype
# Set: b = {1, 2, 3}                    ==>Set: unique & sorted element
# Dictionary: c = {"key": "value"}      ==>Dictionary: similar to c++ map

# single input
x = int(input())

# multiple input
x,y,z = map(int, input().split())

# To input a list and set
arr = list(map(int, input().split()))
sat = set(map(int, input().split()))

# Here, f = f_string. We can write values and string at a time in f string. 
# Let's use it with setprecision
height = 5.67263234
print(f"Hello! My name is shagor.\nI am {height:.3} feet tall.")

# input a n*m Mattrix manually and print it 
n, m = map(int, input().split())
mattrix = []
for i in range(n):
    arr = list(map(int, input().split()))
    mattrix.append(arr)

for i in range(n):
    for j in range(m):
        print(mattrix[i][j], end=" ")
    print()

