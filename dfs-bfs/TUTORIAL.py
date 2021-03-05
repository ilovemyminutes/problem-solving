def dfs(v):
    '''
    부모노드가 v일 때, 왼쪽 자신노드를 v*2, 오른쪽 자식 노드를 v*2 + 1이라 가정
    '''
    if v > 7:
        return
    else:
        # 전위 순회: 기준 노드가 일처리할 거 하고 자식으로 넘어감
        # 대부분 전위 순회를 활용
        print(v)
        dfs(v*2)
        dfs(v*2+1)

        # 중위 순회: 왼쪽 자식으로 가서 일처리 다 하고 나서, "되돌아 와서" 자기의 일 처리
        dfs(v*2)
        print(v)
        dfs(v*2+1)

        # 후위 순회: 왼쪽 오른쪽 자식 모두 처리하고 나서 자기 일 처리
        # 병합 정렬에 활용
        dfs(v*2)
        dfs(v*2+1)
        print(v)