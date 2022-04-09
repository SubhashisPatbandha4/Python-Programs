# PROGRAM: To find the digital root of an integer
# FILE: digital_root.py
# CREATED BY: Subhahsis Patbandha
# DATED: 23/09/20
num = int(input("Enter an integer: "))
temp=num
s=0
while(temp!=0):
    dg=temp%10
    s=s+dg
    temp=temp//10
print("Digital root of ",num," = ",s)
