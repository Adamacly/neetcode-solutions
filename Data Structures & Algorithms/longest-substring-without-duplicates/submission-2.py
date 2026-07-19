class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # lenght = 0
        # for i in range(len(s)):
        #     ch = s[i]
        #     cpt = 1
        #     for j in range(i+1, len(s)):
        #         if s[j] not in ch:
        #             ch+=s[j]
        #             cpt+=1
        #         else:
        #             break
        #     lenght = max(lenght, cpt)
        # return lenght

        l = 0
        length = 0
        s_set = set()
        for r in range(len(s)):
            while s[r] in s_set:
                s_set.remove(s[l])
                l+=1
            s_set.add(s[r])
            length = max(length, r - l + 1)
        return length
                

        