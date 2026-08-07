class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        if nums[low] == target:
            return low
        if nums[high] == target:
            return high
        
        if nums[low] < nums[high]:
            while low < high:
                middle = (low+high) // 2
                if nums[middle] == target:
                    return middle
                if nums[middle] < target:
                    low = middle + 1
                else:
                    high = middle

        low = 0
        high = len(nums)-1

        while low < high:
            middle = (low + high) // 2
            if nums[middle] > nums[high]:
                low = middle + 1
            else:
                high = middle

        break_point = low

        if target == nums[break_point]:
            return break_point
        
        low = 0
        high = len(nums)-1

        while low < high:
            middle = (low + high) // 2               
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                high = break_point
            else:
                low = break_point + 1

        return -1