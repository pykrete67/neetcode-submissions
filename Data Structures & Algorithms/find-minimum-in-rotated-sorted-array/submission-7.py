class Solution:
    def findMin(self, nums: List[int]) -> int:
        # still unsure about this problem, come back later
        low = 0
        high = len(nums)-1
        lowest = 1000 # any num works
        
        while low < high:
            middle = (low + high) // 2

            # rule and trick for this question:
            # if middle > high -> the lowest is in the range of middle to high, it cant possibly be from low to middle
            # else, if middle < high, we set high = middle

            if nums[middle] > nums[high]:
                low = middle + 1
            else:
                high = middle
            
        return nums[low]