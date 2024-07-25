# There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

# Example


# There are two numbers between the arrays: 6 and 12 .
# 6 % 2 = 0,6%6=0 ,  24%6 =0and 36%6=0 for the first value.
# 12%2=0, 12%6=0 and 24%12=0,36%12=0  for the second value. Return 2.

# Sample Input

# 2 3
# 2 4
# 16 32 96
# Sample Output

# 3
# Explanation

# 2 and 4 divide evenly into 4, 8, 12 and 16.
# 4, 8 and 16 divide evenly into 16, 32, 96.

# 4, 8 and 16 are the only three numbers for which each element of a is a factor and each is a factor of all elements of b.

import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_array(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = lcm(result, arr[i])
    return result

def gcd_array(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])
    return result

def getTotalX(a, b):
    lcm_value = lcm_array(a)
    gcd_value = gcd_array(b)
    
    count = 0
    current_multiple = lcm_value
    
    while current_multiple <= gcd_value:
        if gcd_value % current_multiple == 0:
            count += 1
        current_multiple += lcm_value
    
    return count

# Example usage:
a = [2, 4]
b = [16, 32, 96]
print(getTotalX(a, b))  # Output: 3
