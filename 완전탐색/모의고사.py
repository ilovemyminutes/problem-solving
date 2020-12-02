'''https://programmers.co.kr/learn/courses/30/lessons/42840'''

def solution(answers):
    supo_1 = [1, 2, 3, 4, 5] # 5
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    supo_list = [supo_1, supo_2, supo_3]

    best_supo = []
    answer_list = []
    for supo in supo_list:
        pseudo_answer = supo * (len(answers) // len(supo)) + supo[:len(answers)]
        scoring = [i==j for i, j in zip(answers, pseudo_answer)]
        answer_list.append(sum(scoring))

    best_score = max(answer_list)
    for idx, score in enumerate(answer_list):
        if score == best_score:
            best_supo.append(idx + 1)
    return best_supo