class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums.sort()
        # print(nums)
        # longs = []
        # cpt = 1
        # for i in range(1, len(nums)):
        #     if nums[i]==nums[i-1]+1:
        #         cpt+=1 
        #     if nums[i]-nums[i-1]>1:
        #         longs.append(cpt)
        #         cpt=1
        #     if i==len(nums)-1:
        #         longs.append(cpt)
        #     if nums[i]==nums[i-1]:
        #         continue
        # print(longs)
        # if len(nums)==0:
        #     return 0
        # if len(longs)==0:
        #     return cpt
        # return max(longs)
        
        lenghts = [1]
        lenght = 1
        for k in nums:
            if k-1 in nums:
                continue
            else:
                c = k
                while c+1 in nums:
                    lenght+=1
                    c+=1
                lenghts.append(lenght)
                lenght = 1
        if len(nums)==0:
            return 0
        return max(lenghts)