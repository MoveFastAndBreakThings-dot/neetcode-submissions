class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
    
    # Store pair sums with their indices
        pair_sum = {}
        for i in range(n):
            for j in range(i + 1, n):
                s = nums[i] + nums[j]
                if s not in pair_sum:
                    pair_sum[s] = []
                pair_sum[s].append((i, j))
        
        # For each element, look for complement
        for k in range(n):
            target = -nums[k]
            if target in pair_sum:
                for i, j in pair_sum[target]:
                    # Ensure all indices are distinct
                    if i != k and j != k:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        res.add(triplet)
        
        return [list(t) for t in res]
            