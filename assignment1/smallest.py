#accept 2 integers as input and print the smaller using ternary operater
n1=int(input("Enter 1st integer = "))
n2=int(input("Enter 2nd integer = "))
if(n1<=n2):
    small=n1
else:
    small=n2
print("Smallest among ",n1," , ",n2," is ",small)
