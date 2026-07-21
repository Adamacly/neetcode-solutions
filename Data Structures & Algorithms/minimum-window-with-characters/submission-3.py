class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substrings = []
        t_bool = {}
        for c in t:
            t_bool[c] = 1 + t_bool.get(c, 0)
        for l in range(len(s)):
            l_bool = {_:0 for _ in t}
            for r in range(l, len(s)):
                if s[r] in t:
                    l_bool[s[r]] = 1 + l_bool.get(s[r], 0)
                if all(l_bool[i]>=t_bool[i] for i in t):
                    substrings.append(s[l:r+1])
                    break
        res = ""
        print(substrings)
        for i in range(len(substrings)):
            if res=="":
                res = substrings[0]
            if len(substrings[i])<len(res):
                res = substrings[i]
        return res
        