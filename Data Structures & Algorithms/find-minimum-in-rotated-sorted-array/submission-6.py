class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)

        # for i in range(1,len(nums)):
        #     if nums[i]<nums[i-1]:
        #         return nums[i]
        # return nums[0]
        res = nums[0]
        i, j = 0, len(nums)-1
        m = 0
        while(i<=j):
            if nums[i]<=nums[j]:
                return min(res, nums[i])
            m = (i+j)//2
            res = min(nums[m], res)
            if nums[m]>=nums[i]:
                i=m+1
            else:
                j=m-1
        return nums[m]

        

        