class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        lowest = 1000

        while low < high:
            middle = (low + high) // 2
            if nums[low] < nums[high]:
                lowest = min(nums[low], lowest)
                low = middle + 1
            else:
                lowest = min(nums[high], lowest)
                high = middle

        return lowest
                

        