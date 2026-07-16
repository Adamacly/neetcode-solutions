class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # volumes = [0, ]
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         volume = min(heights[i], heights[j])*(j-i)
        #         volumes.append(volume)
        # return max(volumes)
        i = 0
        j = len(heights) - 1
        max_volume = 0
        while i < j:
            min_height = min(heights[i], heights[j])
            volume = min_height*(j-i)
            max_volume = max(max_volume, volume)
            if heights[i]==min_height:
                i+=1
            else:
                j-=1
        return max_volume
        
        