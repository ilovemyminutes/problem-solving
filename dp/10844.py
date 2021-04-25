"""쉬운 계단 수: https://www.acmicpc.net/problem/10844

* DP 구성 방식
{
    1 자리수인 경우: {
        1로 시작하는 계단수 개수: ?,
        2로 시작하는 계단수 개수: ?,
        ...
        9로 시작하는 계단수 개수: ?
    },
    2 자리수인 경우: {
        1로 시작하는 계단수 개수: ?,
        2로 시작하는 계단수 개수: ?,
        ...
        9로 시작하는 계단수 개수: ?
    },
    ...
    100 자리수인 경우: {
        1로 시작하는 계단수 개수: ?,
        2로 시작하는 계단수 개수: ?,
        ...
        9로 시작하는 계단수 개수: ?
    }
}

* 해결 방법: K 자리수인 경우의 계단수 개수를 구해보자.
- K 자리수를 다음과 같이 앞 자리수에 따라 경우를 나눌 수 있음

    1XXX...X
    2XXX...X
    3XXX...X
    ...
    9XXX...X

- 위 각각의 경우에 대해 (K-1) 자리수의 계단수 경우의 수는 다음과 같이 좁힐 수 있음

    1XXX...X
        => 10XX...X --(1)
        => 12XX...X --(2)
    2XXX...X
        => 21XX...X --(3)
        => 23XX...X --(4)
    3XXX...X
        => 32XX...X --(5)
        => 34XX...X --(6)
    ...
    9XXX...X
        => 98XX...X --(7)

- K-1 자리수의 (1)~(7) 경우 각각에 대하여 계단수를 메모이제이션한 DP로부터 추출, 각각의 결과를 합하면 K 자리수의 총 계단수가 됨
- 



"""

DIVISOR = int(1e9)

n = int(input())  # 계단 수를 확인할 자리수
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
