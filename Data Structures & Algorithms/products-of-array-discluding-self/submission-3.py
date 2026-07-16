class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod = 1
        # res = []
        # for i in range(len(nums)):
        #     p = prod
        #     for k in range(i+1,len(nums)):
        #         p*=nums[k] 
        #     res.append(p)
        #     prod*=nums[i]
        # return res

        res = [1]*len(nums)

        for i in range(len(nums)):
            r = res[i]
            res = [k*nums[i] for k in res]
            res[i] = r
        return res
        