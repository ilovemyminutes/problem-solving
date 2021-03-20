'''
HH:MM ~ HH:MM
- HH: 00~23
- MM: 00~59
'''
def time2scalar(timestring: str) -> int:
    '''시각 문자열을 자정으로부터 흐른 시간(분)으로 리턴'''
    hour, minute = map(int, timestring.split(':'))
    scalar = hour * 60 + minute
    return scalar

def scalar2time(timescalar: int) -> str:
    hour = timescalar // 60
    minute = timescalar - hour*60
    time = f'{hour:0>2d}:{minute:0>2d}'
    return time

START, END = 0, 1

num_users = int(input())
intervals = [tuple(map(time2scalar, input().split(' ~ '))) for _ in range(num_users)]

pseudo_start = max(intervals, key=lambda x: x[START])[START]
pseudo_end = min(intervals, key=lambda x: x[END])[END]

if pseudo_start >= pseudo_end:
    print(-1)
else:
    print(f'{scalar2time(pseudo_start)} ~ {scalar2time(pseudo_end)}')
