from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    answer = 0
    curr_weight = 0

    while bridge:
        answer += 1
        curr_weight -= bridge.pop(0)

        if truck_weights:
            if truck_weights[0] + curr_weight <= weight:
                truck = truck_weights.pop(0)
                curr_weight += truck
                bridge.append(truck)
            else:
                bridge.append(0)
    return answer