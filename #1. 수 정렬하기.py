N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

for n in sorted(numbers):
    print(n)