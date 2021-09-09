def solution(phone_book):
    phone_book.sort(key = len)
    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            s = phone_book[i]
            for k in range(len(s)):
                if s[k] != phone_book[j][k]:
                    break
                if k == len(s) - 1:
                    return False
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
