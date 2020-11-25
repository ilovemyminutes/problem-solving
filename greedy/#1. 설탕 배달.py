# 설탕 배달 https://www.acmicpc.net/problem/2839
def get_least_bag(N):
    max_5 = N // 5
    max_3 = (N - max_5*5) // 3
    while True:
        if max_5*5 + max_3*3 == N:
            return max_5 + max_3
        else:
            if max_5 == 0:
                return -1
            max_5 -= 1
            max_3 = (N - max_5*5) // 3

N = int(input())
print(get_least_bag(N))
        