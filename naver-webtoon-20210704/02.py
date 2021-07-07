'''
문제:
    - 'path-sum' 중 최솟값을 return
    - 각 칸에 숫자가 적혀진 RxC의 그리드 그래프 존재
    - 'path-sum': 오른쪽 아래로 이동하기 위한 경로 상의 숫자들의 합

입력:
    - 그래프 RxC: 각각 1 이상 1천 이하
    - 각 칸에 적힌 숫자: 1 이상 1만 이하

생각:
    - 벽이 없으니까, R x C가 가능한 모든 경로
        - 최대 길이가 1천이니까 최대 1백만 번의 연산
        - 완전탐색으로 풀 수 있겠다
        - 아냐 잘못생각함.
        - 다익스트라로 풀어야될거같은데
'''
import heapq

def move_list(loc: tuple, r, c):
    cur_r, cur_c = loc[0], loc[1]
    dr_list, dc_list = [0, 0, -1, 1], [1, -1, 0, 0]
    output = []
    for dr, dc in zip(dr_list, dc_list):
        nxt_r, nxt_c = cur_r + dr, cur_c + dc
        if 0 <= nxt_r < r and 0 <= nxt_c < c:
            output.append((nxt_r, nxt_c))
    return output

def solution(grid):
    INF = int(1e+9)
    num_rows, num_cols = len(grid), len(grid[0])
    prior_que = []
    heapq.heappush(prior_que, (grid[0][0], (0, 0))) # (WEIGHT, LOC)
    weights = [[INF]*num_cols for _ in range(num_rows)]

    while prior_que:
        cur_w, (cur_r, cur_c) = heapq.heappop(prior_que)
        if weights[cur_r][cur_c] < cur_w:
            continue

        for adj_r, adj_c in move_list((cur_r, cur_c), num_rows, num_cols):
            w = grid[adj_r][adj_c]
            cost = cur_w + w
            if cost < weights[adj_r][adj_c]:
                weights[adj_r][adj_c] = cost
                heapq.heappush(prior_que, (cost, (adj_r, adj_c)))
    
    goal_r, goal_c = num_rows-1, num_cols-1
    min_path_sum = weights[goal_r][goal_c]
    return min_path_sum

    
if __name__ == '__main__':
    # sample = [ [1, 2], [3, 4] ] # 7
    sample = [ [1, 8, 3, 2], [7, 4, 6, 5] ] # 19 
    print(solution(sample))