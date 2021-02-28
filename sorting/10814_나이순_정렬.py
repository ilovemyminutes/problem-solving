'''https://www.acmicpc.net/problem/10814'''
import sys
AGE, NAME = 0, 1
n = int(input())

register = []
for _ in range(n):
    age, name = sys.stdin.readline().split()
    register.append((int(age), name))

register.sort(key=lambda x: x[AGE])

for info in register:
    output = f'{info[AGE]} {info[NAME]}'
    sys.stdout.write(output + '\n')
    
