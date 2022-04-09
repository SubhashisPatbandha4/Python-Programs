# PROGRAM : To accept some inputs of different types and print them using positional parameters format i.e. {}
# FILE : positional_parameter.py
# CREATED BY : Subhashis Patbandha
# DATED : 16-09-20

a = int(input("\nEnter an integer value: "))
b = float(input("Enter a float value: "))
c = input("Enter a string: ")
d = complex(input("Enter a complex number : "))
e = bool(input("Enter a boolean value : "))

print("\nPrinting inputed values using positional parameters\n====================================================")
print(" a = {0} \n b = {1} \n c = {2}\n d = {3}\n e = {4}".format(a,b,c,d,e))