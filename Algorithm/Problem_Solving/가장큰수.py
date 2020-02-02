
def solution(numbers):
    ### 숫자를 정렬해야 되는데 
    numbers = (listmap(str,numbers))
    temp=[]
    for i in numbers:
        if len(i)>3:
            temp.append(i*3)
        elif len(i)>2:
            temp.append(i*4)
        elif len(i)>1:
            temp.apeend(i*6)
        else:
            temp.append(i*12)
    for key,val in enumerate(numbers):
            




    return answer

solution([3,2,1])