'''https://programmers.co.kr/learn/courses/30/lessons/43164'''
def solution(tickets:list) -> list:
    graph = get_graph(tickets)
    stack = ['ICN']
    answer = []
    
    while stack: # 스택을 다 털 때까지
        start = stack[-1] # 사전 체크를 위해 조회만!(pop X)
        if start not in graph.keys() or len(graph[start])==0: # 틈새 없이 털었으면 경로로 추가
            answer.append(stack.pop())
        else:
            stack.append(graph[start].pop()) # 아직 덜 털었으면 끝까지 추출
            
    answer.reverse()
    return answer

def get_graph(tickets:list) -> dict:
    result = dict()
    
    # 그래프 생성
    for t in tickets:
        departure, arrival = t
        if result.get(departure, None) is None:
            result[departure] = [arrival, ]
        else:
            result[departure].append(arrival)
            
    # 알파벳 순 정렬
    for r in result.keys():
        result[r].sort(reverse=True)
        
    return result