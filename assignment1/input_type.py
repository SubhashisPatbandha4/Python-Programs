# Program: To accept some inputs of different types and print the values with their type
# File: input_type.py
# Created By: subhashis patbandha
# Dated: 16/09/20

a = int(input("Enter an integer : "))
b = float(input("Enter a float : "))
c = complex(input("Enter a complex number : "))
d = input("Enter a string : ")
e = bool(input("Enter a boolean value : "))

print("\nType of ",a," = ",type(a))
print("Type of ",b," = ",type(b))
print("Type of ",c," = ",type(c))
print("Type of ",d," = ",type(d))
print("Type of ",e," = ",type(e))
