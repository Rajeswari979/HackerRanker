#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    sum1=x1 + v1
    sum2=x2 + v2
    
    if v2 < v1 :
        for i in range(2,10000):
            if sum1 % i == 0 and sum2 % i == 0:
                return "YES"
        
    return "NO"


print(kangaroo(0,3,4,2))
