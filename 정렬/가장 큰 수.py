'''https://programmers.co.kr/learn/courses/30/lessons/42746
* 풀이컨셉: 퀵정렬
'''


def solution(numbers):
    num_str = list(map(str, numbers))
    result = sort(num_str)
    if len(set(result)) == 1 and list(set(result))[0] == '0':
        return '0'
    else:
        return ''.join(sort(num_str))

def sort(num_str):
    if len(num_str) <= 1:
        return num_str
    pivot = num_str[0]
    left_side = [x for x in num_str[1:] if int(pivot+x) < int(x+pivot)]
    right_side = [x for x in num_str[1:] if int(pivot+x) >= int(x+pivot)]
    return sort(left_side) + [pivot] + sort(right_side)



'''
* 풀이컨셉(실패)
(예) [3, 30, 34, 5, 9]
1. 각 원소를 문자열로 변환 후 정렬 => ['9', '5', '34', '30', '3']
2. 원소별 가장 앞 숫자를 기준으로 그룹화, 그룹별 정렬 진행
    i. '9', '5': 유니크하므로 정렬 필요 X
    ii. '34', '30', '3'
        - 앞 숫자가 중복되었을 경우, 뒷 숫자가 큰 것이 가장 앞으로
        - '3'처럼 자릿수가 다를 경우, 앞 숫자를 반복하여('33') 자릿수를 맞춤
        - 이를 바탕으로 그룹별 정렬 진행
'''
def solution(numbers):
    result = list()
    num_sorted = sorted(list(map(lambda x: str(x), numbers)), reverse=True)
    unq_heads = sorted(list(set(map(lambda x: x[0], num_sorted))), reverse=True)

    for u in unq_heads:
        temp = list(filter(lambda x: x.startswith(u), num_sorted))
        if len(temp) == 1:
            result.append(temp[0])
        else:
            max_len = max(map(lambda x: len(x), temp))
            orders = [order[0] for order in \
                sorted([(i, j) for i, j in \
                    enumerate(list(map(lambda x: x + x[-1]*(max_len-len(x)), temp)))], 
                    key=lambda x: x[-1], reverse=True)
                    ]
            for o in orders:
                result.append(temp[o])
    return ''.join(result)


'''실패'''
def solution(numbers):
    # idx_dict = {idx: i for idx, i in enumerate(numbers)}; print(num_with_idx)
    idx_tup = [(idx, i) for idx, i in enumerate(numbers)]
    max_len = max(map(lambda x: len(str(x[-1])), idx_tup)); print(max_len)
    order = get_order(idx_tup, max_len)
    return ''.join([str(numbers[i]) for i in order])


def get_order(idx_tup, max_len):
    padding = tuple(map(lambda x: int(str(x[-1])+str(x[-1])[-1]*(max_len-len(str(x[-1])))), idx_tup))
    padding_indexed = sorted(((idx, num) for idx, num in enumerate(padding)), key=lambda x: x[-1], reverse=True)
    order = [i[0] for i in padding_indexed]
    return order