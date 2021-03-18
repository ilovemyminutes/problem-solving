"""단어 정렬, https://www.acmicpc.net/problem/1181"""
import sys

n = int(input())

sentences = list(set([sys.stdin.readline()[:-1] for _ in range(n)]))

sentences.sort()  # 알파벳 순 정렬
sentences.sort(key=len)  # 길이 순 정렬

for sentence in sentences:
    output = sentence + "\n"
    sys.stdout.write(output)
