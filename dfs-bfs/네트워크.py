"""https://programmers.co.kr/learn/courses/30/lessons/43162"""
#%%
"""네트워크를 밝혀낸다기보다는,
같은 네트워크를 구성하는 컴퓨터를 샅샅히 방문처리한다는 느낌으로 접근
"""


def dfs(computers, visited, start):
    nodes = [start]
    while nodes:
        node = nodes.pop()
        if visited[node] == 0:  # 방문 체크
            visited[node] = 1
        for another in range(len(computers[node])):  # 연결된 노드 탐색
            if computers[node][another] == 1 and visited[another] == 0:
                nodes.append(another)
        print(nodes, visited)


def solution(n, computers):
    answer = 0
    visited = [0] * n
    start = 0
    while 0 in visited:  # 다 방문할 때까지
        if visited[start] == 0:  # 기준점을 방문하지 않은 경우 DFS 진행
            dfs(computers, visited, start)  # 연결된 모든 노드에 대한 방문처리
            answer += 1
        start += 1  # 다음 노드로 넘어감
    return answer


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
