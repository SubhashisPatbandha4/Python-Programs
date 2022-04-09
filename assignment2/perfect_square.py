# PROGRAM: To check a number is a Perfect square or not
# FILE: perfect_square.py
# CREATED BY: Subhashis Patbandha
# DATED: 23/09/20

import math

num = int(input("Enter a number : "))

root = math.sqrt(num)

if( int(root + 0.5)**2 == num):
    print(num,"is a perfect square of ",int(root))

else:
    print(num,"is not a perfect square")