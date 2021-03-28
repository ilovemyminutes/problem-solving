"""피보나치 함수 https://www.acmicpc.net/problem/1003"""
import sys

MAX_N = 40
zero_cnts = [0 for _ in range(MAX_N+1)]
one_cnts = [0 for _ in range(MAX_N+1)]

def count_zero_one(n):
    global zero_cnt, one_cnt
    if n == 0:
        zero_cnts[n] += 1
        zero_cnt = 1
        one_cnt = 1
        return zero_cnt, one_cnt
    elif n == 1:
        one_cnts[n] += 1
        zero_cnt = 0
        one_cnt = 1
        return zero_cnt, one_cnt
    else:
        if zero_cnts[n] != 0 and one_cnts[n] != 0:
            return (zero_cnts[n], one_cnts[n])
        else:
            pre1 = count_zero_one(n-1)
            pre2 = count_zero_one(n-2)
            print(n, pre1, pre2)
            zero_cnt = pre1[0] + pre2[0]
            one_cnt = pre1[1] + pre2[1]
            zero_cnts[n] = zero_cnt
            one_cnts[n] = one_cnt
            return zero_cnt, one_cnt

# t = int(input())
# counts = []
# for _ in range(t):
#     counts.append(count_zero_one(int(sys.stdin.readline())))
print(count_zero_one(2))
# print(zero_cnts, one_cnts)