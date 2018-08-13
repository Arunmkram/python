
#number of uppercase and lowercase letters  in a string
a=input("enter the string")
a=a.replace(" ", "")
count=0
length=len(a)
for i in a:
  if i.isupper():
    count=count+1

upper=count
lower=length-upper
print("uppercase =",upper)
print("lowercase =",lower)