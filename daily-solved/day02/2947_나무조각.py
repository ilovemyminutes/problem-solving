'''https://www.acmicpc.net/problem/2947
문제:
    - 나무조각 5개
    - 조각1 > 조각2 => 스왑
    - 조각2 > 조각3 => 스왑
    - 조각3 > 조각4 => 스왑
    - 조각4 > 조각5 => 스왑
    - 만약 순서가 1, 2, 3, 4, 5 순서가 아니라면 1 단계로 다시 간다.
    
목적: 위치를 바꿀 때마다 조각의 순서를 출력
생각:
    같아질때까지 루프를 돌리면서 출력하면 되겠네
    조건을 순서대로 거쳐야하니까 elif가 아닌 if문을 열거하는게 맞음
'''
woods = list(map(int, input().split()))
ideal = [1, 2, 3, 4, 5]

def print_output(woods):
    output = list(map(str, woods))
    print(' '.join(output))


if woods == ideal:
    pass
else:
    while True:
        if woods[0] > woods[1]:
            tmp = woods[0]
            woods[0] = woods[1]
            woods[1] = tmp
            print_output(woods)

        if woods[1] > woods[2]:
            tmp = woods[1]
            woods[1] = woods[2]
            woods[2] = tmp
            print_output(woods)
        
        if woods[2] > woods[3]:
            tmp = woods[2]
            woods[2] = woods[3]
            woods[3] = tmp
            print_output(woods)

        if woods[3] > woods[4]:
            tmp = woods[3]
            woods[3] = woods[4]
            woods[4] = tmp
            print_output(woods)

        if woods == ideal:
            break


    

    
