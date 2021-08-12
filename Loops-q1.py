n=int(input("Enter number of Fibonacci terms you need: "))
x=0;y=1
print(x,y,sep=', ',end=', ')
for i in range(n-2):
    z=x+y
    print(z,end=', ')
    x=y
    y=z
