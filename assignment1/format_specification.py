# PROGRAM : To accept some inputs of different types and print them using format specification e.g. %
# FILE : format_specification.py
# CREATED BY : Subhashis Patbandha
# DATED : 16-09-20

a = int(input("\nEnter an integer value: "))
b = float(input("Enter a float value: "))
c = input("Enter a string: ")

print("\nPrinting the inputted values using format specification\n==========================================================")

print("a = %d \nb = %.2f \nc = %s" %(a,b,c))