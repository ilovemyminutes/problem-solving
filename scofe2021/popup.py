'''
오른쪽 또는 아래로만 이동 가능
'''
from itertools import permutations

n_cols, n_rows = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n_rows)]
directions = ['right']*(n_cols-1) + ['down']*(n_rows-1)

max_n_clothes = 0

for p in permutations(directions, r=len(directions)):
    loc = [0, 0]
    n_clothes = graph[loc[0]][loc[1]]
    for d in p:
        if d == 'right':
            loc[1] += 1
            n_clothes += graph[loc[0]][loc[1]]

        elif d == 'down':
            loc[0] += 1
            n_clothes += graph[loc[0]][loc[1]]
    if max_n_clothes <= n_clothes:
        max_n_clothes = n_clothes

print(max_n_clothes)





#%%
from functools import reduce
temp = [i for i in range(10000, 10100)]
temp2 = [i for i in range(1, 101)]
reduce(lambda x, y: x*y, temp) / 
