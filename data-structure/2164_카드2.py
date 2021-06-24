'''https://www.acmicpc.net/problem/2164
문제:
    - 카드 수: N (1~N 번호 부여됨)
    - N번이 젤 아래로 가도록 순서대로 쌓여있음
    - 카드 한장남을 때까지 다음을 반복
        (1) 제일 위 카드 버림
        (2) 이후 제일 위 카드를 맨 아래로 이동
'''
from collections import deque
n = int(input())
cards = deque([i for i in range(1, n+1)])

if len(cards) == 1:
    print(cards[0])

else:
    while True:
        cards.popleft() # 삭제
        if len(cards) == 1:
            break
        card = cards.popleft()
        cards.append(card)
    print(cards[0])