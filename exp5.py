from __future__ import print_function

n=int(input("Enter the size of matrix"))

for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==j):
           print("1 ",sep="",end="")
        else:
           print("0 ",sep="",end="") 
    print() 