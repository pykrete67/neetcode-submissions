class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # had a hard time solving this, focus when coming back
        result = [0] * len(temperatures)
        stack = []
        # need to always make sure the list is monotonically decreasing
        for index, item in enumerate(temperatures):
            while stack and stack[-1][0] < item:
                stackItem, stackIndex = stack.pop()
                result[stackIndex] = index - stackIndex
            stack.append([item, index])

        return result



                

        