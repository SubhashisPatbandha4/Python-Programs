'''
to check strong number or not
'''

while(True):
    num=input("\nPlease enter an integer : ")
    if(num.isnumeric()==0):
        print("\n",num," is not an integer !")
        continue
    else:
        num=int(num)
        break
    
temp=num
s=0

while(temp!=0):
    fact=1
    dg=temp%10
    while(dg!=0):
        fact=fact*dg
        dg-=1
    s=s+fact
    temp//=10
    
if(s==num):
    print("\n",num," is a strong number")
else:
    print("\n",num," is not a strong number")
 
    
