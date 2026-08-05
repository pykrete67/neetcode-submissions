class Solution:
    def findMin(self, nums: List[int]) -> int:
        # still unsure about this problem, come back later
        low = 0
        high = len(nums)-1
        lowest = 1000 # any num works
        
        while low < high:
            middle = (low + high) // 2

            # rule and trick for this question:
            # there are always 2 sections in the list, and both are sorted, the goal is to find the breaking point first
            # if middle > high -> the lowest is in the range of middle to high
            # else, if middle < high, we set high = middle

            # since there are 2 sections in the list and both sections need to be sorted, thus if the middle is greater than high, the lowest element cant possibly be in the index before middle because it is sorted. if there is a lower element at a greater index -> the break point needs to be between the middle and high index, thus we assign low to middle + 1. (+ 1 because we dont need to include the middle element)

            if nums[middle] > nums[high]:
                low = middle + 1
            # for else, if the if statement above is false, then the lowest element needs to be in the other section, thus we set the high as middle and we can start searching from there
            else:
                high = middle
            
        return nums[low]