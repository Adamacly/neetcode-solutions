class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def are_anagrams(s: str, t:str) -> bool:
        #     s_dict = {k: 0 for k in s}
        #     t_dict = {k: 0 for k in t}
        #     for k in s:
        #         if k not in t:
        #             return False
        #         s_dict[k]+=1
        #     for k in t:
        #         if k not in s:
        #             return False
        #         t_dict[k]+=1
        #     return s_dict == t_dict

        # out = []
        # for i in range(len(strs)):
        #     if strs[i]==0:
        #         continue
        #     liste = [strs[i]]
        #     for k in range(i+1, len(strs)):
        #         if strs[k]==0:
        #             continue
        #         if are_anagrams(strs[i], strs[k]):
        #             liste.append(strs[k])
        #             strs[k]=0
        #     out.append(liste)
        # return out

        res = defaultdict(list)

        for s in strs:
            count = [0]*26

            for k in s:
                count[ord(k)-ord("a")]+=1
            res[tuple(count)].append(s)
        return list(res.values())

        