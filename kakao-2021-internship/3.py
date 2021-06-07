# n: 처음 표의 행 개수
# k: 처음 선택된 행의 인덱스
# cmd: 명령어가 담긴 문자열 배열


def solution(n, k, cmd):
    status = ['O'] * n
    loc_list = [i for i in range(n)]
    removed = []

    loc = k # 선텍된 인덱스명
    iloc = k # 선택된 인덱스 위치

    for c in cmd:
        if c.startswith('U'):
            _, num_up = c.split()
            iloc -= int(num_up)
            loc = loc_list[iloc]

        elif c.startswith('D'):
            _, num_down = c.split()
            iloc += int(num_down)
            loc = loc_list[iloc]

        elif c == 'C':
            status[loc] = 'X' # 삭제할 인덱스명을 X 표시
            removed.append((loc, iloc)) # 삭제할 인덱스명과 해당 인덱스명의 위치를 기록
            
            # 위치/인덱스명 갱신
            if iloc == (len(loc_list) - 1): # 선택행이 마지막에 위치할 경우
                iloc -= 1 # 위치를 바로 위로 이동

            loc_list.remove(loc) # 삭제
            loc = loc_list[iloc] # 인덱스명 갱신

        elif c == 'Z':
            recover_loc, recover_iloc = removed.pop()
            status[recover_loc] = 'O'
            loc_list.insert(recover_iloc, recover_loc)
            iloc = loc_list.index(loc)

    return ''.join(status)


if __name__ == '__main__':
    n = 8
    k = 2
    cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"] # OOXOXOOO
    print(solution(n, k, cmd))