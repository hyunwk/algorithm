import collections
from typing import List

class Solution:
    def groupAnagram(self, strs: List[str]) ->List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())

strs = ["eat","tea","tan","ate","nat","bat"]
b = Solution()
strs = b.groupAnagram(strs)
for str in strs:
    print(str)