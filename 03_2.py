def solution(arr: list) -> int:
    max_length = 0
    cur_maxlen = 0

    pre_num = None
    ascending = True
    for cur_num in arr:
        if pre_num is None:
            pre_num = cur_num
            cur_maxlen += 1
        else:
            if ascending:
                if pre_num <= cur_num:
                    cur_maxlen += 1
                    pre_num = cur_num
                else:
                    ascending = False
                    cur_maxlen += 1
                    desc_equal = 1
                    pre_num = cur_num
            else:
                if pre_num > cur_num:
                    cur_maxlen += 1
                    desc_equal = 1
                    pre_num = cur_num

                elif pre_num == cur_num:
                    cur_maxlen += 1
                    desc_equal += 1
                    pre_num = cur_num

                else:
                    if max_length < cur_maxlen:
                        max_length = cur_maxlen
                    cur_maxlen = desc_equal + 1 
                    ascending = True
                    pre_num = cur_num

    if max_length == 0:
        max_length = cur_maxlen

    return max_length

if __name__ == '__main__':
    from time import time
    test = [6,4,1,2,3,6,9]
    start = time()
    print(solution(test))
    # print(time() - start)