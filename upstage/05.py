'''
문제:
    - 목적: 최적의 경로로 목적지까지 갈 수 있는 방법
        - 최적의 경로의 우선순위; 준엽이는 돈이 없는 학생이다
            (1) 최소 환승 횟수
            (2) 최소 시간
        - '환승' := 역간 이동시 운영 회사가 바뀔 경우
    - 지하철은 A, B 두 회사가 운영함
    - 경쟁사이기 때문에 사용자가 다른 회사 지하철로 환승할 때마다 운임 비용이 상승

입력:
    - N, M:
        - N: 지하철역 수. 2 이상 1천 이하
            - 지하철역의 번호는 0부터 N-1로 매겨짐
            - 출발지점은 0으로 가정
        - M: 목적지 번호 1 이상 999 이하
    - N줄에 걸쳐 지하철역 번호별 회사
        - 0: 회사 A
        - 1: 회사 B
    - N줄에 걸쳐 연결 관계(시간)
        - 0: 연결되지 않음
        - 1 이상: 해당 숫자만큼의 시간이 걸림

생각:
    - BFS로 훑는데,
        - 도착지에 도달할 때까지 환승횟수, 시간을 저장하고
        - 도착지에 도달했을 때 멈춰
        - 도착지에 도달한 경로 중에서
'''

                                                                                                                                            
class ProblemPy:

    @staticmethod
    def solve(n, e, companies, subway_map):
        # IMPLEMENT HERE
        transfer = 0
        dist = 0

        return transfer, dist

    def get_path(start, end, subway_map) -> tuple:
        if dp[start][end] != (None, None):
            return dp[start][end]

        elif end in subway_map[start]:
            num_trans = 1 if companies[start] != companies[end] else 0
            duration = subway_map[start][end]
            dp[start][end] = (num_trans, duration)
            return (num_trans, duration)
            
        else:
            min_trans = 0
            min_duration = 0

            while end not in subway_map[start]:
                connected = [idx for idx in subway_map[end] if idx != 0]
                tmp_min_trans, tmp_min_duration = 1000, 1000
                for c in connected:
                    tmp_num_trans, tmp_duration = self.get_path(start, c)
                    if tmp_num_trans < tmp_min_trans:
                        tmp_min_trans = tmp_num_trans
                        tmp_min_duration = tmp_duration
                    elif tmp_duration == tmp_min_trans and tmp_duration < tmp_min_duration:
                        tmp_min_duration = tmp_duration
                min_trans += tmp_min_trans
                min_duration += tmp_min_duration

            return (min_trans, min_duration)

# DO NOT MODIFY FROM HERE
n = 6
e = 3
companies = [0, 1, 1, 0, 1, 0]
subway_map = [
    [0, 3, 1, 0, 10, 0], 
    [3, 0, 0, 15, 0, 0], 
    [1, 0, 0, 0, 0, 1], 
    [0, 15, 0, 0, 10, 0], 
    [10, 0, 0, 10, 0, 1], 
    [0, 0, 1, 0, 1, 0]
    ]
print(ProblemPy.solve(n, e, companies, subway_map))