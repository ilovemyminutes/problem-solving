"""
한수: X의 각 자리수가 등차수열을 이루는 수
"""
def is_arith(num) -> bool:
    num = str(num)

    if len(num) == 1 or len(num) == 2:
        return True
    else:
        d = int(num[0]) - int(num[1])
        for i in range(1, len(num)-1):
            if d != int(num[i]) - int(num[i+1]):
                return False
        return True

n = int(input())

answer = 0
for num in range(1, n+1):
    if is_arith(num):
        answer += 1

print(answer)