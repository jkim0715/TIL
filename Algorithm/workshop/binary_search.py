def solution(L, x):
    idx = -1
    lower = 0
    upper = len(L)-1

    while lower <= upper:
        middle = (upper+lower)//2
        
        if L[middle] == x:
            return middle
        elif L[middle] > x:
            upper = middle -1
        elif L[middle] < x:
            lower = middle + 1
    return idx
