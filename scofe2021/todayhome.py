from functools import reduce

n = int(input())
spatial_info = [list(map(int, list(input()))) for _ in range(n)]

def get_space(spatial_info: list, size: int, row: int, col: int):
    space = spatial_info[row: row+size]
    space = list(map(lambda x: x[col:col+size], space))
    return space
    
def is_empty(space: list) -> int:
    if isinstance(space, int):
        return True if space == 1 else False
    else:
        if all(list(map(lambda z: reduce(lambda x, y: x*y, z), space))):
            return True
        else:
            return False

total_cases = 0
num_cases_dict = {}

for size in range(1, n+1):
    num_cases = 0
    num_move = n - size + 1

    for row in range(num_move):
        for col in range(num_move):
            if size >= 2:
                space = get_space(spatial_info, size, row, col)
            else:
                space = spatial_info[row][col]
            if is_empty(space):
                num_cases += 1
    num_cases_dict[size] = num_cases
    total_cases += num_cases

print(f'total: {total_cases}')
for key, value in  num_cases_dict.items():
    if value > 0:
        print(f'size[{key}]: {value}')
