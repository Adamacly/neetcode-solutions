class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s_reverse = reversed(s)
        # return s_reverse==s
        s = s.lower()
        i = 0
        j = len(s) - 1
        while(i<=j):
            if not ("a"<=s[i]<="z" or "0"<=s[i]<="9"):
                i+=1
                continue
            if not ("a"<=s[j]<="z" or "0"<=s[j]<="9"):
                j-=1
                continue
            if s[j]!=s[i]:
                return False
            else:
                i+=1
                j-=1
                print(i, j)
        return True
        