class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return i
        # return -1
        i, j = 0, len(nums)-1
        while(i<=j):
            m = (i+j)//2
            if nums[m]==target:
                return m
            if nums[m]>=nums[i]:
                if target > nums[m] or target < nums[i]:
                    i = m+1
                else:
                    j = m-1
            else:
                if target > nums[j] or target < nums[m]:
                    j = m-1
                else:
                    i = m+1
        return -1
        