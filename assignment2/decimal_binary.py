# PROGRAM: To convert a Decimal number to binary
# FILE: decimal_binary
# CREATED BY: Subhashis Patbandha
# DATED: 23/09/20

num = int(input("\nEnter a Decimal number : "))

bin_value = 0
ctr = 0
temp = num

if(num<0):
    print("\n",num," is not a decimal number")

else: 
    while(num!=0):
        rem = num%2
        c = pow(10,ctr)
        bin_value = bin_value + (rem * c)
        num = num // 2
        ctr = ctr + 1
    print("\nThe binary of ",temp," = ",bin_value)
