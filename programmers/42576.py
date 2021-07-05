import collections 
def solution(participant, completion):
#    dct = collections.defaultdict(int)
#    for item in participant:
#        if item in dct:
#            dct[item] += 1
#        else:
#            dct[item]
#    for item in completion:
#        if item in dct:
#            if dct[item] == 0:
#                del dct[item]
#            else:
#                dct[item] -= 1
#    for k in dct.keys():
#        answer = k
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer)[0]

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]	
print(solution(participant, completion))
