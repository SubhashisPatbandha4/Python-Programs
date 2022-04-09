n=int(input("Enter no. of lines : "))
for i in range(1,n+1):
    for j in range(i,n+1):
        print(end=" ")
    if i%2==1:
        for j1 in range(0,i):
            num=j1%2
            print(num,end=" ")
    else:
        for j1 in range(1,i+1):
            num=j1%2
            print(num,end=" ")
    print()
