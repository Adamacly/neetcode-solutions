class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        longs = []
        cpt = 1
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]+1:
                cpt+=1 
            if nums[i]-nums[i-1]>1:
                longs.append(cpt)
                cpt=1
            if i==len(nums)-1:
                longs.append(cpt)
            if nums[i]==nums[i-1]:
                continue
        print(longs)
        if len(nums)==0:
            return 0
        if len(longs)==0:
            return cpt
        return max(longs)
        