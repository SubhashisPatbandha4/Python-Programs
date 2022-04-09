'''
Assignment - 4.7

PROGRAM    :
FILE       :
CREATED BY :Subhashis Patbandha
DATED      :07/10/2020
'''
def find_sum(num1=0,num2=0,num3=0,num4=0,num5=0):
    sum=num1+num2+num3+num4+num5
    return sum       

p=find_sum()
print("Calculating sum \n===================\nusing 0 numbers = ",p)
p=find_sum(1)
print("using 1 numbers = ",p)
p=find_sum(1,2)
print("using 2 numbers = ",p)
p=find_sum(1,2,3)
print("using 3 numbers = ",p)
p=find_sum(1,2,3,4)
print("using 4 numbers = ",p)
p=find_sum(1,2,3,4,5)
print("using 5 numbers = ",p)
