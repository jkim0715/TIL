def solution(participant, completion):
    for i in completion:
        participant.pop(participant.index(i))

    return ' '.join(participant)




def solution1(participant, completion):
    for i in completion:
        participant.remove(i)


    return participant[0]

print(solution1(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))