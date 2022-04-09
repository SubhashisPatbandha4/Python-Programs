'''
Assignment-2.1

PROGRAM    :To check a number as perfect or not
FILE       :perfect.py
CREATED BY :Subhashis Patbandha
DATED      :23/09/2020

'''
while (True):
    num=input("\nPlease input an Integer : ")
    if(num.isnumeric()==0):
        print("\n",num," is not an integer !")
        continue
    else:
        num=int(num)
        break
temp=num
s=0
for i in range(1,num):
    if(temp%i==0):
        s=s+i
if(s==num):
    print("\n",num," is a perfect number")
else:
    print("\n",num," is not a perfect number")


