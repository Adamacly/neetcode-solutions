import numpy as np
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

        res = np.array([1]*len(nums))

        for i in range(len(nums)):
            r = res[i]
            res = res * nums[i]
            res[i] = r
        return list(res)
        