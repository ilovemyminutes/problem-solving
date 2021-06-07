"""https://www.acmicpc.net/problem/1158"""


n, k = map(int, input().split())
arr = [i for i in range(n)]

cur_idx = 0
interval = k - 1
output = '<'

while arr:
    length = len(arr)
    cur_idx = (cur_idx + interval) % length # 현위치 & 2칸 이동 & 인덱스가 넘치지 않도록 모듈러 연산

    # 다음 시작 번호
    next_val = arr[0] if cur_idx == length - 1 else arr[cur_idx+1]

    # 제거
    killed = arr.pop(cur_idx)
    
    if len(arr) == 0:
        output += str(killed+1) + '>' # 사람번호=인덱스+1
        break
    else:
        output += str(killed+1) + ', '
        cur_idx = arr.index(next_val)
        
print(output)
