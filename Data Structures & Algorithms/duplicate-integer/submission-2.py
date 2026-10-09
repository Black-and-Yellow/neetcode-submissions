class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h_set = set()
        if len(nums) == 0 or len(nums) == 1:
            return False
        for i in range(len(nums)):
            if nums[i] in h_set:
                return True
            h_set.add(nums[i])
        return False