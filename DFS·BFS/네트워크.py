"""https://programmers.co.kr/learn/courses/30/lessons/43162"""
def dfs(computers, visited, start):
    nodes = [start]
    while nodes:
        node = nodes.pop()
        if visited[node] == 0:
            visited[node] = 1
        for another in range(len(computers[node])):
            if computers[node][another] == 1 and visited[another] == 0:
                nodes.append(another)

def solution(n, computers):
    answer = 0
    visited = [0]*n
    start = 0
    while 0 in visited:
        if visited[start] == 0:
            dfs(computers, visited, start)
            answer +=1
        start+=1
    return answer