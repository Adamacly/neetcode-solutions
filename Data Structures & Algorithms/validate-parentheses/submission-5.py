class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = []
        dict_s = {"(":")", "[":"]", "{":"}"}
        for k in s:
            if k in dict_s.values():
                if stack1 and stack1[-1]==k:
                    stack1.pop()
                else:
                    return False
            else:
                stack1.append(dict_s[k])
        return len(stack1)==0

        