"""https://programmers.co.kr/learn/courses/30/lessons/43162"""
#%%
test = [
    [1, 1, 0], 
    [1, 1, 0], 
    [0, 0, 1]
    ] # answer: 2

from collections import deque

def solution(n, computers):
    cnt = 0
    visited = [0] * n
    group = {0}

    while not all(visit):
        for idx in range(n):
        
        dfs(idx, group)
    return

def dfs(origin, nodes):
    '''어디부터 스캔해야할 지 알려줘야겠지'''
    group = set()
    for node_idx in range(origin+1, n):
        is_connect = computers[origin][node_idx]
        if is_connect == 1 and node_idx not in visited:
            group.add(node_idx)

#%%
n = 4
computers = [
    [1, 0, 0, 0], 
    [0, 1, 0, 0], 
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    ]

def solution(n, computers):
    visited = [0] * n

    def get_network(origin: '기준 노드', network: '네트워크'):
        networks = [origin]
        nonlocal visited
        visited[origin] = 1
        print('기준 노드', origin)
        print(visited)
        if origin == n - 1:
            return network

        # origin 노드와 연결된 노드 확인
        for raw_idx, is_connect in enumerate(computers[origin][origin+1:]):
            node = raw_idx + origin + 1 # 노드 번호
            for idx, net in enumerate(networks): # 연결된 노드가 다른 네트워크에 속하는지 확인
                if node in net:
                    print('무야호', net, node)
                    networks[idx].extend(network) # 
                    return

            print('아다리 맞는 노드', node, network)
            if is_connect == 1 and visited[node] == 0:
                network.append(node)
                get_network(node, network)
        return network

    for computer in range(n):
        if visited[computer] == 0:
            print(get_network(computer, [computer]))
    print(networks)
    return len(list(filter(lambda x: x is not None, networks)))


solution(4, computers)

#%%
temp = list()

for idx, asdf in enumerate(temp):
    print(idx, asdf)
    print(asdf)
