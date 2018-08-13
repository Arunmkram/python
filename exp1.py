n=int(input("Enter Number of Elements"))
a=[]

for i in range(0,n):
    elm=int(input("Enter the Element"))
    a.append(elm)

avg=sum(a)/n

print("Average = ",round(avg,2))