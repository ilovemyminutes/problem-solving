'''https://programmers.co.kr/learn/courses/30/lessons/42883'''
#%%
def solution(number, k):
    stack = [number[0]]

    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    
    if k!= 0:
        stack = stack[:-k]
        
    return ''.join(stack)

print(solution(number, k))
#%%
def get_start(removed_idx, num_list):
    if removed_idx == 0:
        return 0
    else:
        return removed_idx - 1

def solution(number, k):
    num_list = list(map(int, list(number)))
    length = len(num_list)
    pseudo_k = 0
    start = 0
    while pseudo_k != k:
        for idx in range(start, length):
            if idx == length - 1:
                break
            else:
                pre, post = num_list[idx], num_list[idx+1]
                if pre < post:
                    del num_list[idx]
                    pseudo_k += 1
                    start = get_start(idx, num_list)
                    break
    return ''.join(list(map(str, num_list)))


# %%
def get_meta(number):
    meta = list()
    combo = 1
    for idx, n in enumerate(number):
        if idx == len(number) - 1:
            meta.append([int(n), combo]) # 값, 연속빈도
        else:
            if n == number[idx+1]:
                combo += 1
            else:
                meta.append([int(n), combo]) # 값, 연속빈도
                combo = 1
    return meta

def decode_meta(meta):
    return ''.join(list(map(lambda x: str(x[0])*x[1], meta)))

def solution(number, k):
    meta = get_meta(number)
    pseudo_k = 0
    while pseudo_k != k:
        for idx in range(len(meta)):
            if idx == len(meta) - 1:
                break
            else:
                pre, post = meta[idx], meta[idx+1]
                if pre[0] < post[0]:
                    pre[-1] -= 1
                    if pre[-1] == 0:
                        del meta[idx]
                    pseudo_k += 1
                    break
    return decode_meta(meta)