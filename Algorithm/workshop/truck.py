def solution(bridge_length, weight, truck_weights):

    ## 다리 구현 
    bridge = [0] * bridge_length
    temp_sum = 0 
    time=0
    weight_sum = 0
    flag = True
    while flag:
        if len(truck_weights) == 0:
            time += bridge_length
            flag = False
            break
        weight_sum-=bridge.pop()    ### 다리위에 올라간 트럭들 무게 sum으로 계산하면 시간초과 남.
        
        if weight_sum + truck_weights[0] <= weight:
            truck= truck_weights.pop(0)
            bridge.insert(0, truck)
            weight_sum += truck
        else:
            bridge.insert(0,0)
        time +=1

    return time
