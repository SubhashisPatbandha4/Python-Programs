# PROGRAM: To find largest among three integer values, given as input
# FILE: largest3.py
# CREATED BY: Subhashis Patbandha
# DATED: 16/09/20

a = int(input("Enter 1st integer : "))
b = int(input("Enter 2nd integer : "))
c = int(input("Enter 3rd integer : "))

if(a>=b):
    if(a>=c):
        print("\n",a," is the largest.")
    else:
        print("\n",c," is the largest.")
else:
    if(b>=c):
        print("\n",b," is the largest.")
    else:
        print("\n",c," is the largest.")