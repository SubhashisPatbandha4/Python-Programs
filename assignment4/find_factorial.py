def rec_fact(x):
    if x==1:
        return 1
    else:
        return (x * rec_fact(x-1))
num=int(input("Enter an integer to find it's factorial : "))
fact=rec_fact(num)
print("Factorial of ",num," = ",fact)
