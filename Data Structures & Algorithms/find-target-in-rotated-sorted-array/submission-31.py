class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # still not fully understood how the high = middle - 1, low <= high, or the high = len(nums) -1 work, need to go over this
        # also this solution isnt the same as neetcode
        
        #steps to solve 1. edge case for if the list is already perfectly sorted -> just normal binary search
        # 2. use the solution from finding min element in rotated sorted array to find the pivot point
        #3. since we found the pivot, use if else statements to determine which of the 2 chunks to go through to find the target then just do binary search
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
                    high = middle

        return -1
