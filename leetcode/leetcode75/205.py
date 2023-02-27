class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # s_dict = {}
        # t_dict = {}
        # for i in range(len(s)):
        #     if s[i] not in s_dict:
        #         if len(s_dict.values()):
        #             s_dict[s[i]] = max(s_dict.values()) + 1
        #         else:
        #             s_dict[s[i]] = 0
                
        #     if t[i] not in t_dict:
        #         if len(t_dict.values()):
        #             t_dict[t[i]] = max(t_dict.values()) + 1
        #         else:
        #             t_dict[t[i]] = 0
        #     if s_dict[s[i]] != t_dict[t[i]]:
        #         return False
        # return True

        return [s.find(i) for i in s] == [t.find(j) for j in t
