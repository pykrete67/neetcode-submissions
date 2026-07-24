class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]

            if (sum > target):
                r -= 1
            if (sum < target):
                l += 1
            if (sum == target):
                return [l+1, r+1]
        

        # brute force approach

        # first = 0
        # second = 1
        # while first <= len(numbers) and second < len(numbers):
        #     if (numbers[first] + numbers[second] == target):
        #         return [first + 1, second + 1]
        #     if (numbers[first] + numbers[second] != target):
        #         second += 1
        #     if (second == len(numbers)):
        #         first += 1
        #         second = first + 1
        #     if (numbers[first] + numbers[second] == target):
        #         return [first + 1, second + 1]
        #     if (second == len(numbers)):
        #         first += 1
        #         second = first + 1
        
