class Solution:
    def findMin(self, nums: List[int]) -> int:
        # still unsure about this, come back later
        low = 0
        high = len(nums)-1
        lowest = 1000 # any num works

        # # only edge case in this problem is when the list is already perfectly sorted
        # # if this is the case, we just return the first element
        # if nums[low] < nums[high]:
        #     return nums[0]
        
        while low <= high:

            if nums[low] < nums[high]:
                lowest = min(lowest, nums[low])
                break
            middle = (low+high) // 2
            lowest = min(nums[middle], lowest)
            if nums[middle] >= nums[low]:
                low = middle + 1
            else:
                # lowest = min(nums[high], lowest)
                high = middle - 1

        return lowest