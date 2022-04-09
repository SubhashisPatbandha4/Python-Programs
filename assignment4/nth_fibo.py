'''
Assignment - 4.5

PROGRAM    :To find nth fibonaccy term a using recursive function ..
FILE       :nthfibo.py
CREATED BY :Subhashis Patbandha
DATED      :07/10/2020
'''
def nthfibo(n):

    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return nthfibo(n-1)+nthfibo(n-2)

while True:
    n=input("Enter which term you want to find from fibonaccy series :  ")
    if (n.isnumeric()==0):
        print("Error ! Please enter a valid input.\n")
        continue
    elif int(n) < 1 :
        print("Error ! Please enter a valid input.\n")
        continue
    else:
        n=int(n)
        break
nth=nthfibo(n)
print(nth)
 
