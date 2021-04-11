"""문제 출처: https://www.acmicpc.net/problem/9184"""
import sys

dp = dict()

def w(a: int, b: int, c: int) -> int:
    if (a, b, c) in dp:
        return dp[(a, b, c)]
    else:
        if a <= 0 or b <= 0 or c <= 0:
            dp[(a, b, c)] = 1
            return dp[(a, b, c)]

        elif a > 20 or b > 20 or c > 20:
            dp[(a, b, c)] = w(20, 20, 20)
            return dp[(a, b, c)]

        elif a < b and b < c:
            dp[(a, b, c-1)] = w(a, b, c-1)
            dp[(a, b-1, c-1)] = w(a, b-1, c-1)
            dp[(a, b-1, c)] = w(a, b-1, c)
            return dp[(a, b, c-1)] + dp[(a, b-1, c-1)] - dp[(a, b-1, c)]

        else:
            dp[(a-1, b, c)] = w(a-1, b, c)
            dp[(a-1, b-1, c)] = w(a-1, b-1, c)
            dp[(a-1, b, c-1)] = w(a-1, b, c-1)
            dp[(a-1, b-1, c-1)] = w(a-1, b-1, c-1)
            return dp[(a-1, b, c)] + dp[(a-1, b-1, c)] + dp[(a-1, b, c-1)] - dp[(a-1, b-1, c-1)]


END = (-1, -1, -1)
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if (a, b, c) == END:
        break
    else:
        print(f"w({a}, {b}, {c}) = {w(a, b, c)}")