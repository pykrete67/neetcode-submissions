class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = set(nums)
        if len(temp) < len(nums):
            return True

        return False
        