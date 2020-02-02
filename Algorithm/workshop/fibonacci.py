def solution(x):
    if x < 2:
        return x
    else:
        temp1 =0
        temp2 =1
        for _ in range(2,x+1):
            ans = temp1 + temp2
            temp1 = temp2
            temp2 = ans

    return ans