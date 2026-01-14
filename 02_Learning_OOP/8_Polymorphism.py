# The word Polymorphism means "many forms" and it refers to the methods/functions with the
# same name that can be executed on many form or objects or classes. here, the sum is a
# polymorphic function as we can write it in different way. like: sum(2, 3) or sum(3,4,2)
# Note: the len function of python also a polymorphic function as we know that through the 
# len function we can find list, string, set size etc.

def sum(x,y,z=0):
	return x+y+z

print(sum(2,5))
print(sum(2,3,7))
