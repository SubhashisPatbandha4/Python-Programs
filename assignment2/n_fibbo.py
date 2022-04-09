#2.7 to find first n fibonacci numbers
n=int(input("\nEnter range to find fibbonacci series = "))
ctr=2
f1=0
f2=1

if n<1:
    print("\nInvalid range . Please enter a valid range !")
else:
    print("\nFirst ",n," fibbonacci numbers are = ",end="")
    if n==1:
        print(f1)
    elif n==2:
        print(f1,",",f2,end="")
    else:
        print(f1,",",f2,end="")
        while(ctr<n):
            f3=f1+f2
            print(",",f3,end="")
            f1=f2
            f2=f3
            ctr=ctr+1
    
    
