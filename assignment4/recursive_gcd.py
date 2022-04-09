def recursive_gcd(n1,n2):
    if n1==n2:
        return n1
    elif n1 > n2:
        return recursive_gcd(n1-n2,n2)
    else:
        return recursive_gcd(n1,n2-n1)
n=int(input("\nEnter number : "))
gcd_val = n

while True:
    n = int(input("\nEnter another number : "))
    gcd_val=recursive_gcd(gcd_val,n)
    ch=input("\nWant more Input(Y/N)? : ")
    if ch=='y' or ch=='Y' :
        continue
    else:
        break
print("\nGCD = ",gcd_val)
