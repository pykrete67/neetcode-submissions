class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row of target first using binary search (still iffy, focus on this first phase when coming back)
        low = 0
        high = len(matrix)

        while low < high:
            middle = (low + high) // 2
            # if target == nums[middle]:
            #     return middle
            if target >= matrix[middle][0]:
                low = middle + 1
            else:
                high = middle

        # return -1
        row_index = low - 1
        if row_index < 0:
            return False

# -------------------------------------------------------------------------------------------

        # this approach is O(M+LOG(N)) because linear search is done to find the row, we can reduce it to O(log(M*N)) by using binary search to search for the row too
        # row_index = -1

        # for index, item in enumerate(matrix):
        #     if item[0] > target:
        #         row_index = index - 1
        #         break
        
        # print(row_index)

# -------------------------------------------------------------------------------------------

        # find target within the row
        low = 0
        high = len(matrix[row_index])

        while low < high:
            middle = (low + high) // 2
            if target == matrix[row_index][middle]:
                return True
            elif target > matrix[row_index][middle]:
                low = middle + 1
            else:
                high = middle

        return False

        # old solution: the for loop isnt needed
        # for n in matrix:
        #     while low < high:
        #         middle = (low + high) // 2
        #         if target == matrix[row_index][middle]:
        #             return True
        #         elif target > matrix[row_index][middle]:
        #             low = middle + 1
        #         else:
        #             high = middle

        #     return False

# -------------------------------------------------------------------------------------------
        # another solution i thought of at first but didn't know how to implement -> treat the matrix as one sorted flattened list

        # no_of_rows = len(matrix)
        # no_of_cols = len(matrix[0])
        # low = 0
        # high = no_of_rows * no_of_cols

        # while low < high:
        #     middle = (low + high) // 2
        #     # formula for pretending 2D array as 1D array 
        #     if target == matrix[middle // no_of_cols][middle % no_of_cols]:
        #         return True
        #     elif target > matrix[middle // no_of_cols][middle % no_of_cols]:
        #         low = middle + 1
        #     else:
        #         high = middle

        # return False