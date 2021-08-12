x=input("Enter list of numbers separated by space:")
List=x.split(' ')
L=[]
print("List: ",List)
print("The positive numbers in List are: ")
for i in List:
    if int(i)>=0:
       L.append(int(i))
print(L)
