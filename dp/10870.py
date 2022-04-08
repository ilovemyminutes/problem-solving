n = int(input())

dp = [0, 1]

for t in range(n+1):
    if t < 2:
        continue

    v = dp[t-1] + dp[t-2]
    dp.append(v)

print(dp[n])