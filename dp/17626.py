"""자연수 n이 주어질 때 제곱수의 합으로 표현하는 최소 개수를 출력
50000개까지니까 미리 다 만들어둬도 될 것 같은데
"""
import math

dp = [None] * 50001  # 1부터 최소개수
dp[1] = 1

def get_min_nums(num: int):
    if dp[num] is not None:
        return dp[num]
    else:
        max_div = int(math.sqrt(num))
        if max_div == 1:
            min_num = num
        else:
            candidates = []
            for d in [max_div - i for i in range(max_div)]:
                q = num // (d**2)
                if q > 4:
                    break

                res = num - q * (d**2)
                cand_min_num = q + get_min_nums(res) if res > 0 else q
                
                if cand_min_num <= 4:
                    candidates.append(cand_min_num)
            min_num = min(candidates)

        dp[num] = min_num
        return min_num

n = int(input())
print(get_min_nums(n))