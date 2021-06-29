import heapq

def find_max_sum(numbers):
    if len(numbers) >= 2:
        sum_ = 0
        big1, big2 = 0, 0
        for idx, n in enumerate(numbers):
            if idx == 0:
                big1 = n

            elif idx == 1:
                if n >= big1:
                    big2 = big1
                    big1 = n
                else:
                    big2 = n
            else:
                if big1 <= n:
                    big2 = big1
                    big1 = n
                elif big2 <= n < big1:
                    big2 = n
                else:
                    pass
            sum_ = big1 + big2 
    else:
        sum_ = sum(numbers)

    return sum_
    
if __name__ == "__main__":
    print(find_max_sum([5, 9, 7, 9, 11 ]))