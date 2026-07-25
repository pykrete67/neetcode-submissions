class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = 1
        while first < len(numbers):
            if (numbers[first] + numbers[second] == target):
                return [numbers[first], numbers[second]]
            if (numbers[first] + numbers[second] != target):
                second += 1
            if (numbers[second] == len(numbers) - 1):
                first += 1
        