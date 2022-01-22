def get_table(s):
    table = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = table[j - 1]
        if s[i] == s[j]:
            j += 1
            table[i] = j
    return table


def kmp(haystack, needle):
    if haystack == needle or not needle:
        return 0
    table = get_table(needle)
    print(table)
    j = 0

    for i in range(len(haystack)):
        print(i, j)
        while j > 0 and haystack[i] != needle[j]:
            j = table[j - 1]
        if haystack[i] == needle[j]:
            if j == len(needle) - 1:
                return i - j
            j += 1
    return -1
