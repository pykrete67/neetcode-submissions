class Solution:
    def findMin(self, nums: List[int]) -> int:
        # still unsure about this problem, come back later
        low = 0
        high = len(nums)-1
        lowest = 1000 # any num works
        
        while low <= high:

            # only edge case in this problem is when the list is already perfectly sorted
            if nums[low] < nums[high]:
                lowest = min(lowest, nums[low])
                break
            middle = (low+high) // 2
            lowest = min(nums[middle], lowest)
            if nums[middle] >= nums[low]:
                low = middle + 1
            else:
                high = middle - 1

        return lowest