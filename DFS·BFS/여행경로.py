'''https://programmers.co.kr/learn/courses/30/lessons/43164
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
'''
#%%
# tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']] # return [ICN, JFK, HND, IAD]
tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]


def flatten(arr: list, unique: bool=False) -> list:
    result = list()
    
    for a in arr:
        result.extend(a) if isinstance(a, list) else result.append(a)

    return list(set(result)) if unique else result
flatten(tickets, unique=False)

visited = [0] * len(flatten(tickets, unique=True)); print(visited)
start = 'ICN'


#%%
def dfs(graph, start, end): 
    """DFS 를 이용하여 미로 찾기 알고리즘을 구현한다. 
    :param graph: 미로 그래프 
    :param start: 출발 지점(노드) 
    :param end: 도작 지점(노드) 
    :return: 최소 이동 거리
    """ 
    stack = [(start, 0)] # idx 0: 노드, idx 1: 이동 거리 
    visit = {start, } # 방문한 노드 저장 공간 
    while stack: 
        node, distance = stack.pop(); print('노드', node, '현재까지 거리', distance, end=' ')
        print('인접노드', graph[node])
        new_distance = distance + 1; print('전진! 갱신된 거리', new_distance)
        for near_node in graph[node]: # 방문한 적 없는 노드인 경우 
            if near_node not in visit: 
                print("{} Node 첫 발견".format(near_node), end=' ') 
                
                # 도착 지점에 도착한 경우 총 이동거리를 반환 
                if near_node == end: 
                    return new_distance 
                
                visit.add(near_node) # 방문 
                stack.append((near_node, new_distance)) # 이동 거리를 1 증가 시킨다. 
                print('Stack', stack)
                
    return -1 # 도착 지점이 막힌 경우(없는 경우)

graph = { 
    "A": ["B"], 
    "B": ["A", "C"], 
    "C": ["B", "D"], 
    "D": ["C", "E"], 
    "E": ["D", "F"], 
    "F": ["E", "G"], 
    "G": ["F", "J"], 
    "H": ["I"], 
    "I": ["H", "P"], 
    "J": ["G", "K", "O"], 
    "K": ["J", "L"], 
    "L": ["K", "M"], 
    "M": ["L"], 
    "N": ["O"], 
    "O": ["J", "N", "P"], 
    "P": ["I", "O"] 
    }

dfs(graph, 'A', 'M')

#%%
def solution(tickets):
    t = dict()
    for ticket in tickets:
        if ticket[0] in t:
            t[ticket[0]].append(ticket[1])
        else:
            t[ticket[0]] = [ticket[1]]
    print(t)

    for k in t.keys():
        t[k].sort(reverse=True)

    st = ["ICN"]
    answer = []

    while st: 
        top = st[-1]
        print(st, top)


        if top not in t or len(t[top]) ==0:
            print(top, '다 돌았다')
            answer.append(st.pop())

        else:
            temp = t[top].pop()
            print('아직 안돌아서 스택에 추가', top, '에 대한 도착지', temp)
            
            st.append(temp)
        print('정보', t)
        print('현재 경로', answer)

    answer.reverse()
        
    return answer

tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'],
['ATL', 'ICN'], ['ATL', 'SFO'], ]
solution(tickets)