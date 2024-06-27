
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    
    while x1 != x2:
        x1 += v1
        x2 += v2        
    
    if x1 == x2:
        return 'YES'
    else:
        return 'NO'

print(kangaroo(0,3,4,2))
