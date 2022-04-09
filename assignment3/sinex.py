
num=int(input("\nEnter the value of x in degree : "))
n=int(input("\nEnter value of n : "))
x=(num*3.14)/180
s=0
sign=1
ctr=1
print("\nsin ",num," = ",end="")
for i in range(1,n+1,2):
    temp=x
    fact=1
    power=i
    while(power!=0):
        fact=fact*power
        power=power-1
    term=( (x**i)/fact)*sign
    if(ctr%2==0):
        print("-",end="")
    else:
        print("+",end="")
    print("(%.6f"%x**i,"/",i,"!)",end="")

    s=s + term
    sign=sign*-1
    ctr=ctr+1

print(" = %.6f"%s)
