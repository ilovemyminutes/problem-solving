def get_feature(graph_genre, preferences, row: int, col: int):
    genre = graph_genre[row][col]
    rate = preferences[genre]
    return [genre, rate, row, col]

def make_tidy(r: list) -> str:
    output = ' '.join(list(map(str, r)))
    return output


genres = ['A', 'B', 'C', 'D', 'E']
rates = list(map(float, input().split()))
preferences = {}
for i, rate in enumerate(rates):
    preferences[genres[i]] = rate

n, m = list(map(int, input().split())) # row 수, column 수
graph_state = [list(input()) for _ in range(n)] # state: W(완전 열람), O(불완전 열람), Y(미열람)
graph_genre = [list(input()) for _ in range(n)] # genre: A ~ E

recommends = {'Y': [], 'O': []}
for row in range(n):
    for col in range(m):
        if graph_state[row][col] == 'Y': # 미열람
            recommends['Y'].append(get_feature(graph_genre, preferences, row, col))
            
        elif graph_state[row][col] == 'O': # 불완전 열람
            recommends['O'].append(get_feature(graph_genre, preferences, row, col))

for k in ['Y', 'O']:
    if recommends[k]:
        recommends[k].sort(key=lambda x: x[1], reverse=True)
        for r in recommends[k]:
            print(make_tidy(r))