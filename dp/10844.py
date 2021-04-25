"""쉬운 계단 수: https://www.acmicpc.net/problem/10844"""

DIVISOR = int(1e9)

n = int(input())  # n 자리수
dp = {i: {j: 0 for j in range(0, 10)} for i in range(1, 101)}


def get_stair_first_digit(first_digit):
    if first_digit == 9:
        return [8]
    else:
        return [first_digit - 1, first_digit + 1]


for k in range(1, n + 1):  # k번째 자리수
    if k == 1:  # 자리수 1의 경우 예외 처리
        for m in range(1, 10):
            dp[k][m] += 1
    else:
        for cur_first_digit in range(1, 10):  # 자리수가 k인 자연수의 가장 첫번째 자리수 (0~9)
            pre_stair_num_first_digits = get_stair_first_digit(
                cur_first_digit
            )  # 조건에 맞는 두번째 자리수 추출

            for (
                first_digit
            ) in pre_stair_num_first_digits:  # 자리수가 k-1이고 가장 앞자리가 first_digit인 수의 개수 추출
                if first_digit == 0:
                    if k == 2:
                        dp[k][cur_first_digit] += 1
                    else:
                        dp[k][cur_first_digit] += dp[k - 2][1]
                else:
                    dp[k][cur_first_digit] += dp[k - 1][first_digit]

print(sum(dp[n].values()) % DIVISOR)
