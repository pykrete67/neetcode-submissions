class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = 1
        while first <= len(numbers) and numbers[second] <= len(numbers):
            if (numbers[first] + numbers[second] == target):
                return [first + 1, second + 1]
            if (numbers[first] + numbers[second] != target):
                second += 1
            if (numbers[first] + numbers[second] == target):
                return [first + 1, second + 1]
            if (second == len(numbers)):
                first += 1
                second = first + 1
        