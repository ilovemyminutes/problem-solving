"""신입 사원, https://www.acmicpc.net/problem/1946"""

n_test = int(input("# Test Case:"))  # 테스트 케이스
score_all_test = []
for _ in range(n_test):
    score_one_test = []
    n_applicant = int(input("# Applicant:"))  # 지원자 수
    for _ in range(n_applicant):
        paper_face = input("Scores:")  # 'X Y' 꼴
        paper, face = paper_face.split(" ")[0], paper_face.split(" ")[1]
        score_one_test.append((paper, face))
    score_all_test.append(score_one_test)
