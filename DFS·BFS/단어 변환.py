#%%
'''
1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.

예를 들어 begin이 hit, target가 cog, words가 [hot,dot,dog,lot,log,cog]라면
hit -> hot -> dot -> dog -> cog와 같이 4단계를 거쳐 변환할 수 있습니다.
'''
begin = 'hit' # 루트 노드
target = 'cog'
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

# begin = 'hit'
# target = 'hhh'
# words = ['hhh','hht', 'hot']


def solution(begin, target, words):
    if target not in words:
        print('설마')
        return 0
    length = len(begin)
    stack = [begin]
    visited = []
    n_changes = 0
    pre_adj = []

    diff_num = 0
    while stack:
        s = stack.pop(); print(s)
        if s in visited:
            continue
        diff = [(idx, sum([i==j for i, j in zip(s, word)])) for idx, word in enumerate(words)]
        begin_diff = [(idx, sum([i==j for i, j in zip(begin, word)])) for idx, word in enumerate(words)]
        adj_1 = set(map(lambda x: words[x[0]], filter(lambda x: x[-1]==length-1, diff))) # 인접 노드
        adj_2 = set(map(lambda x: words[x[0]], filter(lambda x: x[-1]==length-1-diff_num, begin_diff)))
        adj = list(adj_1.intersection(adj_2))
        print('기준', s, '인접', adj)

        if target in adj:
            print('찾', stack)
            n_changes += 1
            return n_changes
        else:
            for a in adj:
                if a not in visited:
                    stack.append(a)
            if s in pre_adj and s in visited:
                print('추가 안할게')
                pass
            else:
                n_changes += 1
            visited.append(s)
            pre_adj = adj.copy()
            print('방문', visited, '스택', stack)
            # pre_adj.remove(s)
            diff_num += 1
    return 0 

solution(begin, target, words)

#%%
s = stack.pop()
visited.append(s)
print('기준', s)

diff = [(idx, sum([i==j for i, j in zip(list(s), list(word))])) for idx, word in enumerate(words)]
print(diff)
adj = list(map(lambda x: words[x[0]], filter(lambda x: x[-1]==2, diff))) # 인접 노드
print('인접1', adj)

if target in adj:
    print('찾았다', adj)

for a in adj:
    if a not in visited:
        stack.append(a)
        visited.append(a)
# adj: diff의 값이 1인 것!

s = stack.pop()
visited.append(s)
print('기준', s)

diff = [(idx, sum([i==j for i, j in zip(s, word)])) for idx, word in enumerate(words)]
adj = list(map(lambda x: words[x[0]], filter(lambda x: x[-1]==2, diff))) # 인접 노드
print('인접2', adj)

if target in adj:
    print('찾았다', adj)

for a in adj:
    if a not in visited:
        stack.append(a)
        visited.append(a)

s = stack.pop()
visited.append(s)
print('기준', s)

diff = [(idx, sum([i==j for i, j in zip(s, word)])) for idx, word in enumerate(words)]
adj = list(map(lambda x: words[x[0]], filter(lambda x: x[-1]==2, diff))) # 인접 노드
print('인접3', adj)

if target in adj:
    print('찾았다', adj)

for a in adj:
    if a not in visited:
        stack.append(a)
        visited.append(a)

print(stack, visited)

s = stack.pop()
visited.append(s)
print('기준', s)

diff = [(idx, sum([i==j for i, j in zip(s, word)])) for idx, word in enumerate(words)]
adj = list(map(lambda x: words[x[0]], filter(lambda x: x[-1]==2, diff))) # 인접 노드
print('인접3', adj)

if target in adj:
    print('찾았다', adj)

for a in adj:
    if a not in visited:
        stack.append(a)
        visited.append(a)
