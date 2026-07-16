class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        res = []
        for i in nums:
            freqs[i]+=1
        print(freqs)
        k_vals = sorted(list(freqs.values()))[-k:]
        for key in freqs.keys():
            if freqs[key] in k_vals:
                res.append(key)
        return res