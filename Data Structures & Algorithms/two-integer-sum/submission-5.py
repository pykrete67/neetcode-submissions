class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = set(nums)

        for i in range(len(nums)):
            if (target - nums[i]) in temp:
                j = nums.index(target - nums[i], i+1, len(nums))
                return([i, j])