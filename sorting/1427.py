"""소트인사이드, https://www.acmicpc.net/problem/1427"""

n = list(input())
n.sort(reverse=True)
print("".join(n))
