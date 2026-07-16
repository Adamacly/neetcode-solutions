class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = []
        dict_s = {"(":")", "[":"]", "{":"}"}
        if len(s)%2!=0:
            return False
        for k in s:
            if k in dict_s:
                stack1.append(dict_s[k])
            else:
                if len(stack1)==0:
                    return False
                c = stack1.pop()
                if k!=c:
                    return False
        return len(stack1)==0

        