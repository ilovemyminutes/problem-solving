from collections import Counter

def solution(s):
    iloc_dict = dict()
    for idx, char in enumerate(list(s)):
        iloc = iloc_dict.get(char, None)
        if iloc is None:
            iloc_dict[char] = idx

    result_iloc = len(s)
    for char, cnt in Counter(s).items():
        # 최초 갱신
        if cnt == 1 and iloc_dict[char] < result_iloc:
            result_iloc = iloc_dict[char]
            
    if result_iloc == len(s):
        return -1
    else:
        return result_iloc + 1 
            
if __name__ == '__main__':
    print(solution('hackthegame'))