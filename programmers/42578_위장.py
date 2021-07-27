def solution(clothes):

    from collections import Counter
    dct = Counter([kind for name, kind in clothes])

    answer = 1
    for val in dct.values():
        answer *= (val+1)
    return answer - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"],["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
