'''
Assignment - 4.8

PROGRAM    :To define a single function to find product of 4 numbers max and implement in main program.
FILE       :product4.py
CREATED BY :Subhashis Patbandha
DATED      :07/10/2020
'''
def product(num1=0,num2=1,num3=1,num4=1):
    p=num1*num2*num3*num4
    return p        

p=product()
print("calculating product \n===================\nusing 0 numbers = ",p)
p=product(2)
print("using 1 numbers = ",p)
p=product(2,4)
print("using 2 numbers = ",p)
p=product(2,4,6)
print("using 3 numbers = ",p)
p=product(2,4,6,8)
print("using 4 numbers = ",p)
