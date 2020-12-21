"""https://programmers.co.kr/learn/courses/30/lessons/43162"""
#%%
n = 3
computers = [
    [1, 1, 0], 
    [1, 1, 0], 
    [0, 0, 1]
    ]

adj = [
    [1],
    [0],
    [],
]

#%%
graph = [
    [1, 1, 0], 
    [1, 1, 0], 
    [0, 0, 1]
    ]
graph = [
    [1, 1, 0], 
    [1, 1, 1], 
    [0, 1, 1]
    ]

visited = []
networks = []

stack = [0]
n = 0

'''
첫 노드부터 순서대로 훑어
연결관계 파악해
graph = [
    [1, 1, 0], => 1번째 노드: 2
    [1, 1, 1], => 2번째 노드: 1, 3
    [0, 1, 1]  => 3번째 노드: 2
    ]
걸린 다른 노드들에 대해서 dfs를 해보는거지
뭘할건데
1번째 노드 -> 2번째 노드 -> 1, 3번째 노드 -> 1번은 방문했으니 3번째 노드만 -> 모두 방문했으니 종료
완전 다른 네트워크가 생길 수도 있잖아

이 문제는 단순히 탐색에 대한 것이 아니라, 네트워크 개수에 대한 문제

네트워크가 여러개일 수 있는데, 단위 네트워크의 연결 관계를 dfs로 밝혀내는게 핵심
'''

networks = []
visited = []
ndim = graph
# for n in ndim:
n = 0
network = {n}
visited.append(n) # n번째 노드는 방문

def solution(n, graph):
    networks = []
    for node in range(n):
        network = {node}
        connected = list(map(lambda x: x[0], filter(lambda x: x[-1] == 1, [(idx+node+1, v) for idx, v in enumerate(graph[node][node+1:])])))
        network = network.union(set(connected))
        if any(map(lambda x: node in x, networks)):
            to_union = networks.index(list(filter(lambda x: node in x, networks))[0])
            networks[to_union] = networks[to_union].union(network)
        else:
            networks.append(network)
    return len(networks)


networks = solution(3, graph)
networks

#%%
from collections import deque

def bfs(computers,check, i, n):
    dq = deque()
    dq.append(i)

    while len(dq)>0:
        curIndex = dq.pop()
        check[curIndex]= True
        for k in range(0,n):
            if check[k] ==False and computers[curIndex][k]==1: 
                dq.append(k) 
    print(dq)


def solution(n, computers):
    answer = 0
    check = [False for i in range(n)]
    print(check)
    for i in range (0, n):
        if check[i] == False:
            bfs(computers, check, i, n)

            answer+=1
    return answer

#%%
solution(3, graph)