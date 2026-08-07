class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        lowest = 1000 # any num works

        if nums[low] == target:
            return low
        if nums[high] == target:
            return high
        while low < high:
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] > nums[high]:
                low = middle + 1
            else:
                high = middle

        return -1