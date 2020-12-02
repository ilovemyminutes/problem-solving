'''https://programmers.co.kr/learn/courses/30/lessons/42842'''

def solution(brown, yellow):
    b_side_len = brown + 4 # brown 총 둘레
    for i in range(1, (b_side_len // 2) + 1):
        b_width = (b_side_len - 2*i) // 2 # brown 가로 길이
        b_height = (b_side_len - 2*b_width) // 2 # brown 세로 길이

        y_width = b_width - 2 # yellow 가로 길이
        y_height = b_height - 2 # yellow 세로 길이

        if y_width < 0 or y_height < 0: # 길이가 음수인 경우
            continue

        pseudo_y = y_width * y_height # 설정된 가로, 세로 길이에 따른 y 칸 갯수
        if pseudo_y == yellow:
            break
    return [b_width, b_height]