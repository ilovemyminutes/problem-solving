n = int(input())
path = list(input())

def move(loc: int, path: list):
    CAN_VISIT = '1'
    move_length = [1, 2] # 1칸, 2칸
    movable_list = [loc+d for d in move_length if (loc+d <= len(path)-1) and (path[loc+d] == CAN_VISIT)]
    return movable_list

num_cases = 0
start = 0

def search_paths(path: list, loc: int, arrival: int):
    global num_cases
    
    movable_list = move(loc, path)
    for m in movable_list:
        if m == arrival: # 도착
            num_cases += 1
            return
        search_paths(path, m, arrival)
        print(f'Loc: {m}, Cases: {num_cases}')


search_paths(path=path, loc=start, arrival=len(path)-1)
print(num_cases)