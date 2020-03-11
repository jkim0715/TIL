def solution(progresses, speeds):
    answer = []

    progresses.append(0)
    speeds.append(0)
    while len(progresses)>1:
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        cnt = 0
        print(progresses)
        if progresses[0] >= 100:
            while len(progresses)>0:
                if progresses[0] >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    cnt +=1
                else:
                    answer.append(cnt)
                    break
            
    return answer

print(solution([93,30,55],[1,30,5]))


