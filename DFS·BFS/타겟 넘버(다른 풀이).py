'''
문제 출처: https://programmers.co.kr/learn/courses/30/lessons/43165
'''

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

solution(k, i)=solution(k+numbers[i], i+1)+solution(k-numbers[i], i+1)