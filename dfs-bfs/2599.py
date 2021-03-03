"""짝 정하기, https://www.acmicpc.net/problem/2599"""
# 같은 초등학교 출신이 아닌 남학생과 여학생을 짝으로 정한다
import copy

MALE, FEMALE = "M", "F"
reverse = {MALE: FEMALE, FEMALE: MALE}
CATS = ["A", "B", "C"]


def get_adj(origin: tuple, members: dict) -> list:
    """짝을 찾아주는 함수"""
    comp = set(members.keys()) - {origin[0]}
    return [(c, reverse[origin[-1]]) for c in comp if members[c][reverse[origin[-1]]]]


def check_remain(members: dict) -> bool:
    """짝이 빠짐없이 지어졌는지 확인"""
    return True if sum(map(lambda x: sum(x.values()), members.values())) else False


def get_pairs(members_raw: dict) -> dict:
    """출력 형태에 맞게 답을 도출"""
    answer = {a: [0, 0] for a in CATS}
    for class_ in CATS:
        comp = sorted(list(set(members_raw.keys()) - {class_}))
        for idx, c in enumerate(comp):
            value = min([members_raw[class_][MALE], members_raw[c][reverse[MALE]]])
            members_raw[class_][MALE] -= value
            members_raw[c][reverse[MALE]] -= value
            answer[class_][idx] += value
    return answer


# get input <- 에러 발생 지점
n_students = int(input())
members_raw = dict().fromkeys(CATS)
for idx in range(3):
    m, f = map(int, input().split(" "))
    nums = {MALE: int(m), FEMALE: int(f)}
    members_raw[CATS[idx]] = nums

members = copy.deepcopy(members_raw)

# DFS
# 시작: 적어도 한명인 경우 임의로 하나 추출
for k in members.keys():
    if members[k][MALE] > 0:
        stack = [(k, MALE)]
        break
    elif members[k][FEMALE] > 0:
        stack = [(k, FEMALE)]
        break

while stack:
    origin = stack.pop()
    if members[origin[0]][origin[-1]] == 0:
        continue
    else:
        members[origin[0]][origin[-1]] -= 1
    stack.extend(get_adj(origin, members))

# 결과 출력
if check_remain(members):
    print(0)
else:
    print(1)
    for v in get_pairs(members_raw).values():
        print(v[0], v[1])
