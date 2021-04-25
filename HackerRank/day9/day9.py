import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)