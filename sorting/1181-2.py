"""
- 길이 짧은 것부터
- 길이 같으면 철자순

단어수: 1~2만, 문자열은 50자까지
"""
import sys

input = sys.stdin.readline

n = int(input())
data = []
wordcheck = dict()
for _ in range(n):
    word = input().strip()
    length = len(word)
    if wordcheck.get(word, False) is False:
        data.append((length, word))
        wordcheck[word] = True

data.sort(key=lambda x: x[1])
data.sort(key=lambda x: x[0])

for (_, w) in data:
    print(w)
