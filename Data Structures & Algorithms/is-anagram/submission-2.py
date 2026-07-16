class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict_s = {k: 0 for k in s}
        dict_t = {k: 0 for k in t}
        for k in s:
            if k not in t:
                return False
            else:
                dict_s[k]+=1
        for k in t:
            if k not in s:
                return False
            dict_t[k]+=1
        return dict_t == dict_s
        