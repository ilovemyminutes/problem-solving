"""https://www.acmicpc.net/problem/2805
절단기 높이 H
H보다 높은 나무 - 잘림
H보다 낮은 나무 - 잘림
잘려 떨어진 윗부분을 가져감
=> 가져가는 나무 길이의 총 합이 최종 나무 길이
나무를 최대한 적게 자르면서 원하는 만큼의 길이를 가져갈 수 있도록 H를 최대화
"""
n, m = map(int, input().split())
trees = list(map(int, input().split()))

min_, max_ = 0, max(trees)

while min_ <= max_:
    mid = (min_ + max_) // 2

    # 잘린 길이를 더해보는 과정
    total_length = 0
    for h in trees:
        if h >= mid:
            total_length += h - mid

    # 지정 길이보다 많이 잘린 경우: H를 높임
    if total_length >= m:
        min_ = mid + 1
    
    # 지정 길이보다 적게 잘린 경우: H를 낮춤
    else:
        max_ = mid - 1

print(max_)



