#factors(n)

lower=int(input("Enter lower limit"))
upper=int(input("Enter Upper limit"))

n=int(input("Enter the divisor"))

for i in range(lower,upper+1):
    if(i%n==0):
       print(i)