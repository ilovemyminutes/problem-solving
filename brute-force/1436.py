'''https://www.acmicpc.net/problem/1436
종말의 숫자: 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수
'''
n = int(input())

SPECIAL_NUM = '666'
title = 0
pseudo_n = 0

while n != pseudo_n:
    title += 1
    if SPECIAL_NUM in str(title):
        pseudo_n += 1

print(title)