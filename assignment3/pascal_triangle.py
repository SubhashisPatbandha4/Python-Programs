n=int(input("\nEnter number of lines to print pascle triangle : "))
for r in range(0,n):
    for c in range(n-r,1,-1):
        print(" ",end="")
    temp=1
    num=r
    den=1
    for c1 in range(0,r+1):
        print(temp,end=" ")
        temp=temp*num
        temp=temp//den
        num=num-1
        den=den+1

    print()
