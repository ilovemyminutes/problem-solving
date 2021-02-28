'''
문제 출처: https://programmers.co.kr/learn/courses/30/lessons/43165
내 풀이: 타겟 넘버를 구하는 과정을 역으로 생각해서 가능한 경우를 탐색
(예) numbers = [1,1,1,1,1], target = 3
numbers의 앞 성분부터 가져와서 target 값에 덧셈 또는 뺄셈을 진행
트리의 윗 갈래는 뺄셈, 아랫 갈래는 덧셈에 대한 경우를 따짐
3┌2┌1┌0┌-1┌-2
 │ │ │ │  └0(Good Case) <- numbers의 모든 성분들의 역연산이 진행된 결과값이 0이면 적절한 케이스
 │ │ │ └1┌0(Good Case)
 │ │ │   └2
 │ │ └2┌1┌0(Good Case)
 │ │   │ └2
 │ │   └3┌2
 │ │     └4
 │ └3┌2┌1┌0(Good Case)
 │   │ │ └2
 │   │ └3┌2
 │   │   └4
 │   └4┌2┌1
 │     │ └3
 │     └4┌3
 │       └5
 .
 .
 .
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