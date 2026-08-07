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
                elif nums[middle] < target:
                    low = middle + 1
                else:
                    high = middle - 1

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

        if target == nums[break_point-1]:
            return break_point - 1

        low = 0
        high = len(nums)

        if target > nums[low] and target < nums[break_point-1]:
            high = break_point
        else:
            low = break_point

        while low < high:
                middle = (low+high) // 2
                if nums[middle] == target:
                    return middle
                elif nums[middle] < target:
                    low = middle + 1
                else:
                    high = middle - 1

        return -1
