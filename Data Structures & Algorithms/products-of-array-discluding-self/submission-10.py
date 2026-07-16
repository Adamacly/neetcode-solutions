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

        # res = [1]*len(nums)

        # for i in range(len(nums)):
        #     r = res[i]
        #     res = [k*nums[i] for k in res]
        #     res[i] = r
        # return res
        pre = [nums[0]]
        post = [nums[-1]]
        res = []
        for i in range(1, len(nums)):
            pre.append(pre[i-1]*nums[i])
            post.insert(0, post[-i]*nums[-i-1])
        res.append(post[1])
        for i in range(1, len(nums)-1):
            res.append(pre[i-1]*post[i+1])
        #print(pre, post, res)
        res.append(pre[-2])
        return res
        