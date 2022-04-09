def reverse(num):
    rev = 0
    while(num!=0):
        dg=num%10
        rev=rev*10+dg
        num=num//10
    return rev
n=int(input("Enter a number : "))
rev=reverse(n)
print("Reverse of ",n," = ",rev)
        
