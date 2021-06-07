PERSON = 'P'
PARTITION = 'X'
MAX_LEN = 5
DIST1 = [
    [0, 0, -1, +1], 
    [+1, -1, 0, 0]
    ] # 상, 하, 좌, 우

DIST2 = [
    [0, 0, -2, +2, +1, +1, -1, -1], 
    [+2, -2, 0, 0, -1, +1, -1, +1]]

ROW = 0
COL = 1

def solution(places):
    answers = []

    for place in places:
        graph, p_positions = get_meta_info(place)
        answer = check_right(graph, p_positions)
        answers.append(answer)

    return answers


def check_right(graph, p_positions):
    if len(p_positions) == 0:
        return 1

    for p_position in p_positions:
        # dist 1
        adj_positions = get_adj_position_dist1(p_position)
        for adj in adj_positions:
            if graph[adj[ROW]][adj[COL]] == PERSON:
                return 0

        # dist 2
        adj_positions = get_adj_position_dist2(p_position)
        for adj in adj_positions:
            if graph[adj[ROW]][adj[COL]] == PERSON:

                # case 2: 길이가 2인 정사각형 모양
                if adj[ROW] != p_position[ROW] and adj[COL] != p_position[COL]:
                    check_pos_1 = (adj[ROW], p_position[COL])
                    check_pos_2 = (p_position[ROW], adj[COL])
                    if (graph[check_pos_1[ROW]][check_pos_1[COL]] != PARTITION 
                        or graph[check_pos_2[ROW]][check_pos_2[COL]] != PARTITION):
                        print(graph[check_pos_1[ROW]][check_pos_1[COL]])
                        print(graph[check_pos_2[ROW]][check_pos_2[COL]])
                        return 0
                else:
                    if adj[ROW] == p_position[ROW]:
                        check_pos = (p_position[ROW], int((p_position[COL]+adj[COL])/2))
                    elif adj[COL] == p_position[COL]:
                        check_pos = (int((p_position[ROW]+adj[ROW])/2), p_position[COL])

                    if graph[check_pos[ROW]][check_pos[COL]] != PARTITION:
                        print(graph[check_pos[ROW]][check_pos[COL]])
                        return 0
    return 1

def get_meta_info(place):
    graph = []
    p_positions = []

    for row_idx, p in enumerate(place):
        row_sequence = list(p)
        p_positions.extend([(row_idx, col_idx) for col_idx, value in enumerate(row_sequence) if value == PERSON])
        graph.append(row_sequence)

    return graph, p_positions
            

def get_adj_position_dist1(p_position):
    adj_positions = []
    row, col = p_position
    for d_row, d_col in zip(*DIST1):
        if row+d_row < 0 or row+d_row >= MAX_LEN or col+d_col < 0 or col+d_col >= MAX_LEN:
            continue
        adj_positions.append((row+d_row, col+d_col))
    return adj_positions

def get_adj_position_dist2(p_position):
    adj_positions = []
    row, col = p_position
    for d_row, d_col in zip(*DIST2):
        if row+d_row < 0 or row+d_row >= MAX_LEN or col+d_col < 0 or col+d_col >= MAX_LEN:
            continue
        adj_positions.append((row+d_row, col+d_col))
    return adj_positions
    


if __name__ == '__main__':
    places = [["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(places))