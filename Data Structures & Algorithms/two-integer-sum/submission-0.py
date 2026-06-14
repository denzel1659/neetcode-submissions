class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx,num in enumerate(nums):
            sol = target - num
            if sol in seen:
                return [seen[sol],idx]
            seen[num] = idx
