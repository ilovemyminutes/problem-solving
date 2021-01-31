"""https://www.acmicpc.net/problem/1946"""
import sys
import copy

def get_cumultive_minimum(rank: list) -> list:
    global INTERVIEW

    answer = []
    for i in range(len(rank)):
        if i == 0:
            MIN = rank[i][INTERVIEW]
        else:
            pseudo_MIN = rank[i][INTERVIEW]
            if pseudo_MIN < MIN:
                MIN = pseudo_MIN
        answer.append(MIN)    
    return answer


PAPER, INTERVIEW = 0, -1
answer = []
t = int(input())

for _ in range(t):
    N = int(input())
    rank = []

    N_FAILS = 0
    rank = sorted(
        [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)],
        key=lambda x: x[PAPER],
    )

    cumultive_min_list = get_cumultive_minimum(rank)

    for idx in range(len(rank)):
        if rank[idx][INTERVIEW] > cumultive_min_list[idx]:
            N_FAILS += 1

    answer.append(N - N_FAILS)

for a in answer:
    print(a)


"""실패: 시간복잡도 O(n^2)
PAPER, INTERVIEW = 0, -1
answer = ''
t = int(input())

for _ in range(t):
    N = int(input())
    rank = []

    N_FAILS = 0
    rank = deque(
        sorted(
            [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)],
            key=lambda x: x[PAPER],
        )
    )
    
    loop_idx = 1
    while len(rank) > 1:
        applicant = rank.popleft()
        for compare in copy.deepcopy(rank):
            if applicant[INTERVIEW] < compare[INTERVIEW]:
                rank.remove(compare)
                N_FAILS += 1
        
    answer += str(N - N_FAILS) + '\n'

print(answer[:-1])
"""
