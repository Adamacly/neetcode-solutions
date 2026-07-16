class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for c in strs:
            s += str(len(c))+ "#"+c
        return s

    def decode(self, s: str) -> List[str]:
        i=0
        res = []
        while i < len(s):
            c = s[i]
            k = i+1
            while s[k]!="#":
                c +=s[k]
                k+=1
            res.append(s[k+1:k+int(c)+1])
            i = k + int(c) + 1

        return res
