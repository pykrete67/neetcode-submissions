class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row of target first
        row_index = -1

        for index, item in enumerate(matrix):
            if item[0] > target:
                row_index = index - 1
                break
        
        print(row_index)

        low = 0
        high = len(matrix[row_index])
        for n in matrix[row_index]:

            while low < high:
                middle = (low + high) // 2
                if target == matrix[row_index][middle]:
                    return True
                elif target > matrix[row_index][middle]:
                    low = middle + 1
                else:
                    high = middle

            return False