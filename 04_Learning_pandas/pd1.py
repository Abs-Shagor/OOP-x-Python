import pandas as pd

mat = [["shagor",1,25,5.6],["Joy",2,24,5.6],["Sami",3,16,5.3],["Alam",4,55,5.7],["Ruma",5,45,5.1]]

mat = pd.DataFrame(mat,columns=["Name","ID","Age","Height"])
# to read a csv file,we can use: mat = pd.read_csv("file path or location")
print(mat)
print("----------------------------------")
print(mat.head(1)) # if we don't put any value, it will show first 5 row
print("----------------------------------")
print(mat.tail(2))
print("----------------------------------")
print(mat.shape) # row and colum size
print("----------------------------------")
print(mat.columns) # all colum name
print("----------------------------------")
print(mat.dtypes) # colum data type
print("----------------------------------")
print(mat["Age"]) # or print(mat.Name),  to see a specific colum ex. name,age,id etc
print("----------------------------------")
print(mat.loc[2]) # to see a specific row
print("----------------------------------")
print(mat.loc[[1,3]]) # to see multiple row
print("----------------------------------")
print(mat[mat.Age>30]) # row filtering
