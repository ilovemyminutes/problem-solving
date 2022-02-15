"""N번째 종말의 수"""

n = int(input())

num = 0
m = 0
while m != n:
    num += 1
    if '666' in str(num):
        m += 1
print(num)
