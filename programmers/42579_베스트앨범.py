def solution(genres, plays):
    dct = {}
    answer = []
    for idx in range(len(genres)):
        if genres[idx] in dct:
            dct[genres[idx]][0] += plays[idx]
            dct[genres[idx]][1].append((plays[idx], idx))
        else:
            dct[genres[idx]] = [plays[idx], [(plays[idx], idx)]]

    for genre in sorted(dct.values(), reverse=True):
        one_genre = sorted(genre[1], key = lambda x: -x[0])
        if len(one_genre) == 1:
            answer.append(one_genre[0][1])
        else:
            for i in range(2):
                answer.append(one_genre[i][1])
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]	
plays =[500, 600, 150, 800, 2500]	
print(solution(genres, plays))
