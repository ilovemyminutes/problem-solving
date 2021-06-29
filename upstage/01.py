from collections import Counter

def find_unique_numbers(numbers: list):
    uniques = [num for num, cnt in Counter(numbers).items() if cnt == 1]
    return uniques