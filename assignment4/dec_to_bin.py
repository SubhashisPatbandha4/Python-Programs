def dec_to_bin(num):
    if num > 1:
        dec_to_bin(num//2)
    print(num%2,end="")
        

n=int(input("Enter a decimal number : "))
print("Binary value of ",n," = ",end="")
dec_to_bin(n)

