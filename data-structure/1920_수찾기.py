def binary_search(sequence, target, start_idx, end_idx):
    """전체: sequence 오름차순 정렬"""
    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2

        if sequence[mid_idx] == target:
            return True
        
        # 가운데값이 target보다 크거나 같을 경우: 우측 절반 버림
        elif sequence[mid_idx] >= target:
            end_idx = mid_idx - 1
            return binary_search(sequence, target, start_idx, end_idx)
        
        # 가운데값이 target보다 작을 경우: 좌측 절반 버림
        else:
            start_idx = mid_idx + 1
            return binary_search(sequence, target, start_idx, end_idx)

    return False

n = int(input())
numbers = sorted([int(i) for i in input().split()])

m = int(input())
queries = [int(q) for q in input().split()]

for q in queries:
    if binary_search(numbers, q, start_idx=0, end_idx=n-1):
        print(1)
    else:
        print(0)