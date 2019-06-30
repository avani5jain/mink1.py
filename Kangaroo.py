import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2,n):
    c=x1
    d=x2
    
    for i in range(0,n):
        c=c+v1
        d=d+v2
    if(c==d):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])
    n=int(input())

    result = kangaroo(x1, v1, x2, v2,n)

    fptr.write(result + '\n')

    fptr.close()
