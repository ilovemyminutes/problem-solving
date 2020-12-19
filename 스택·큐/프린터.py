from collections import deque

def solution(priorities, location):
    priorities = deque([(idx, p) for idx, p in enumerate(priorities)])
    pr_copy = priorities.copy()

    result = list()
    while len(pr_copy) > 0:
        state = pr_copy.popleft()
        check = tuple(filter(lambda x: x[-1] > state[-1], pr_copy))
        if check:
            pr_copy.append(state) # 뒤에 다시 추가
        else:
            result.append(state)
    target_value = tuple(filter(lambda x: x[0]==location, priorities))[0]
    return result.index(target_value) + 1