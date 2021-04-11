"""피보나치 함수 https://www.acmicpc.net/problem/1003"""
dp = [None for _ in range(41)] # [(zero_cnt for a_k, one_cnt for a_k) | k = 0, 1, ..., 40]

def calc_zero_one(n: int) -> tuple:
    global dp

    if dp[n] is not None:
        return dp[n]
    else:
        if n == 0:
            dp[n] = (1, 0)
            return (1, 0)
        elif n == 1:
            dp[n] = (0, 1)
            return (0, 1)
        else:
            term1 = calc_zero_one(n-1)
            dp[n-1] = term1
            term2 = calc_zero_one(n-2)
            dp[n-2] = term2

            # elementwise addition
            output = (term1[0]+term2[0], term1[1]+term2[1])
            dp[n] = output
            return output
    

t = int(input())
numbers = [int(input()) for _ in range(t)]
for num in numbers:
    print(*calc_zero_one(num))