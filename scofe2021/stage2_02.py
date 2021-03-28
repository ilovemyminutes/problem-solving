'''
양방향 연결
World Link는 무조건 가능 보장
연결은 최대 20,000
6
seoul beijing 3
beijing hawaii 10
seoul tokyo 4
seoul hawaii 6
tokyo hawaii 5
beijing tokyo 5
'''
N = int(input())
connections = []

for _ in range(N):
    n1, n2, cost = input().split()
    connections.append(({n1, n2}, int(cost)))

connections.sort(key=lambda x: x[-1])
connections = list(map(lambda x: (tuple(x[0]), x[1]), connections))
visited_edge = []
visited_city = []
path = []

edge, cost = connections[0]
while connections:
    visited_edge.append(edge)
    for city in edge:
        if city not in visited_city:
            visited_city.append(city)
    path.append((edge, cost))

    connected = []
    for (c1, c2), cost in connections:
        if (c1, c2) not in visited_edge and c1 not in visited_city:
            connected.append(((c1, c2), cost))
        elif (c1, c2) not in visited_edge and c2 not in visited_city:
            connected.append(((c1, c2), cost))

    if connected: # 있으면 가장 저렴이로
        edge, cost = min(connected, key=lambda x: x[-1])
    else: # 없으면 end
        break

answer = 0
for p in path:
    answer += p[-1]
print(answer)