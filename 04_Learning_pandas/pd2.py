import pandas as pd

mat = [["shagor",1,25,5.6],["Joy",2,24,5.6],["Sami",3,16,5.3],["Alam",4,55,5.7],["Ruma",5,45,5.1]]

mat = pd.DataFrame(mat,columns=["Name","ID","Age","Height"])

print(mat)
print("----------------------------------")
# to add a new column
mat["address"] = ["Dhaka","Kuwait","Chittagong","Kuwait","Chittagong"]
print(mat)
print("----------------------------------")
#to delete or drop a colum
mat = mat.drop(columns="address") #or we can use: del mat["address"]
print(mat)
print("----------------------------------")
# to add or insert a colum in a specific index
mat.insert(2,"address", ["Dhaka","Kuwait","Chittagong","Kuwait","Chittagong"])
print(mat)
print("----------------------------------")
# to rename a colum
mat = mat.rename(columns={"address" : "Address"})
print(mat)
print("----------------------------------")
#to add a new row
mat.loc[5] = ["xyz",11,"ctg",100,6.1]
print(mat)
# to delet a row
mat = mat.drop(5)
print("----------------------------------")
print(mat)