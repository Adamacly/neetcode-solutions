class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, total, liste):
            if total > target or i >= len(nums):
                return 
            if total == target:
                res.append(liste.copy())
                return
            
            liste.append(nums[i])
            backtrack(i, total+nums[i], liste)
            liste.pop()
            backtrack(i+1, total, liste)
        backtrack(0, 0, [])
        return res
        