STR2NUM = dict(
    zero=0,
    one=1,
    two=2,
    three=3,
    four=4,
    five=5,
    six=6,
	seven=7,
 	eight=8,
 	nine=9
    )

def solution(s):
    s = s.lower()
    for literal, num in STR2NUM.items():
        s = s.replace(literal, str(num))
    return int(s)

if __name__ == '__main__':
    solution("one4seveneight")