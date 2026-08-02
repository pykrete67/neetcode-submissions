class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for index, item in enumerate(temperatures):
            while stack and stack[-1][0] < item:
                stackItem, stackIndex = stack.pop()
                result[stackIndex] = index - stackIndex
            stack.append([item, index])

        return result



                

        