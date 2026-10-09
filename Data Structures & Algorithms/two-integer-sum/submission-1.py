class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {n : i for i, n in enumerate(nums)}
        for i,n in enumerate(nums):
            if target - n in h_map and i != h_map[target-n]:
                return [i, h_map[target-n]]
    