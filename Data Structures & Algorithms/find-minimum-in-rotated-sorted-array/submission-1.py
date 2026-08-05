class Solution:
    def findMin(self, nums: List[int]) -> int:
        # still unsure about this, come back later
        low = 0
        high = len(nums)-1
        lowest = 1000 # any num works

        while low <= high:
            middle = (low+high) // 2
            lowest = min(nums[middle], lowest)
            if nums[middle] > nums[low]:
                low = middle + 1
            else:
                # lowest = min(nums[high], lowest)
                high = middle - 1

        return lowest