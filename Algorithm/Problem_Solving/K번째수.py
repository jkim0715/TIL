def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        L = array[i-1:j]
        L.sort()
        ans = L[k-1]
        answer.append(ans)
        print(L)
    print(answer)
    return answer

solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])

