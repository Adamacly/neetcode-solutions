class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenght = 0
        for i in range(len(s)):
            ch = s[i]
            cpt = 1
            for j in range(i+1, len(s)):
                if s[j] not in ch:
                    ch+=s[j]
                    cpt+=1
                else:
                    break
            if cpt>lenght:
                lenght = cpt
        return lenght
        