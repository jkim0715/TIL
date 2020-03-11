visited = []
computer=[]
count = 0

def search(start_com):
    global computer
    global count
    if start_com in visited:
        return

    visited.append(start_com)

    for i in range(len(computer[start_com])):
        if i == start_com:
            continue
        if computer[start_com][i] == 1:
            search(i)
   

def solution(n, computers):
    global count
    global computer
    global visited
    computer = computers
    answer = 0

    for i in range(len(computers)):
        if i not in visited:
            count+=1
        search(i)

    return count

solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]])