def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]


'''실패1'''
def solution(participant, completion):
    for c in completion:
        participant.remove(c)
    return participant[0]

def get_hash(name):
    return sum(map(ord, list(name)))

def get_idx(name, num_element: '참가 명단 수'):
    return get_hash(name) % num_element

def get_hashtable(num_element: '참가 명단 수'):
    return {i:list() for i in range(num_element)}

'''실패2'''
def solution(participant, completion):
    N = len(participant)
    table = [(get_idx(name, N), name) for name in participant]
    for name in completion:
        if name in map(
            lambda x: x[-1], 
            filter(
                lambda x: x[0]==get_idx(name, N), table
                )
                ):
                participant.remove(name)
    return participant[0]

def get_hash(name):
    return sum(map(ord, list(name)))

def get_idx(name, num_element: '참가 명단 수'):
    return get_hash(name) % num_element

'''실패3'''
def solution(participant, completion):
    if len(set(participant) - set(completion)) == 1: # Unique
        return list(set(participant) - set(completion))[0]
    else:
        unq = list(set(participant))
        count_dict = {name: participant.count(name) for name in unq}
        check = map(lambda x: x[0], sorted(count_dict.items(), key=lambda x: x[-1], reverse=True))
        for name in check:
            if count_dict[name] != completion.count(name):
                return name

'''실패4'''
def solution(participant, completion):
    if len(set(participant) - set(completion)) == 1: # Unique
        return list(set(participant) - set(completion))[0]
    else:
        unq = list(set(participant))
        count_dict = {name: participant.count(name) \
        if participant.count(name) == 1 else: name + str(participant.count(name))
            for name in unq}
        check = map(lambda x: x[0], sorted(count_dict.items(), key=lambda x: x[-1], reverse=True))
        for name in check:
            if count_dict[name] != completion.count(name):
                return name
'''실패5'''
def solution(participant, completion):
    if len(set(participant) - set(completion)) == 1:
        return list(set(participant) - set(completion))[0]
    else:
        inv_encode = dict()
        temp_participant = list()
        for p in set(participant):
            if participant.count(p) > 1:
                temp_participant.append(p * participant.count(p))
                inv_encode[p * participant.count(p)] = p
            else:
                temp_participant.append(p)
        return inv_encode[list(set(temp_participant) - set(completion))[0]]

'''실패6'''
def solution(participant, completion):
    srt_part, srt_comp  = sorted(participant), sorted(completion)
    copy_part = srt_part[:] 
    for idx in range(len(srt_part)):
        pseudo = srt_part.pop(idx)
        if srt_part == srt_comp:
            return pseudo
        else:
            srt_part = copy_part[:]