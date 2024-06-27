def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 <= v2:
        return "NO"
    elif x2 < x1 and v2 <= v1:
        return "NO"
    elif x1 == x2 and v1 == v2:
        return "YES"
    else:
    
        if (x1 - x2) % (v2 - v1) == 0:
            return "YES"
        else:
            return "NO"
