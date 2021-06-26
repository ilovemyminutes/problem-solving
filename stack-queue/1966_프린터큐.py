'''https://www.acmicpc.net/problem/1966
문제:
    - 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인
    - 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 적어도 하나 있는 경우
      이 문서를 출력하지 않고 Queue의 가장 뒤에 재배치
      - 그렇지 않을 경우 출력

입력:
    - 테스트 케이스 수
    - 테스트케이스별 첫째 줄: 문서 개수 N, 타깃문서의 index M
                 두번째 줄: N개 문서의 중요도 1~9 중복 가능

출력:
    - 타깃문서가 몇 번째로 출력되는지
'''
import sys
from collections import deque
input = sys.stdin.readline

# initialize
t = int(input())
tests = []

for _ in range(t):
    n, m = map(int, input().split())
    indices = [i for i in range(n)]
    sequence = map(int, input().split())
    tmp = dict(n=n, m=m, sequence=sequence, indices=indices)
    tests.append(tmp)

# solve
for test in tests:
    n, m = test['n'], test['m'] # num documents, target idx
    sequence = deque(test['sequence'])
    indices = deque(test['indices'])
    print_order = 1
    while sequence:
        popped = sequence.popleft()
        idx = indices.popleft()

        # 꺼낸 문서의 중요도가 남은 문서들의 그것보다 모두 크거나 같을 경우 => 프린트
        if all(s <= popped for s in sequence):
            if idx == m:
                break
            print_order += 1
        
        # 꺼낸 문서의 중요도가 남은 문서들의 그것보다 모두 작을 경우 => 끝으로 이동
        else:
            sequence.append(popped)
            indices.append(idx)
    print(print_order)


    