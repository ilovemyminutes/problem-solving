numbers = [1,1,1,1,1]
target = 3
layer = [target]

def solution(numbers, target):
    layer = [target]
    for idx in range(len(numbers)):
        temp = []
        for value in layer:
            if idx == len(numbers) - 1:
                if (value - numbers[idx] == 0) or (value + numbers[idx] == 0):
                    temp.append(0)
                else:
                    pass
            else:
                temp.append(value - numbers[idx])
                temp.append(value + numbers[idx])
        layer = temp[:]
    return len(layer)

print(solution([1,1,1,1,1], 3))