"""https://programmers.co.kr/learn/courses/30/lessons/43162"""
#%%
n = 3
computers = [
    [1, 1, 0], 
    [1, 1, 0], 
    [0, 0, 1]
    ]
# for d in range(len(computers)):
# computers[d][d] = -1

networks = dict()
network_id = 0
row_idx = 0

list(map(lambda x: x == 1, computers[0]))


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

visited.append(n)

def solution(n, computers):
    networks = []
    for n in range(len(computers)):
        network = {n}
        for idx, k in enumerate(computers[n][n+1:]):
            if k == 1:
                network.add(idx+n+1)
        if networks:
            for idx, n in enumerate(networks):
                if n.intersection(network):
                    networks[idx] = n.union(network)
                else:
                    networks.append(network)
        else:
            networks.append(network)
    return len(networks)