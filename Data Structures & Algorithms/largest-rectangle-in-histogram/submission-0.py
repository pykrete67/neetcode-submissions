class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Stores indices of bars (heights[index])
        max_area = 0
        
        # Append a sentinel height of 0 to ensure all bars in the stack are processed.
        heights_ext = heights + [0] 
        N = len(heights_ext)

        for i in range(N):
            current_height = heights_ext[i]
            
            # While the stack is not empty AND the current bar is shorter than 
            # the bar represented by the top of the stack, we have found a potential right boundary.
            while stack and heights_ext[stack[-1]] > current_height:
                # 1. Pop the bar whose height defines the rectangle (H)
                h_index = stack.pop()
                height = heights_ext[h_index]
                
                # 2. Determine the width:
                # The right boundary is the current index 'i'.
                # The left boundary is the bar remaining at the stack top (stack[-1]).
                if not stack:
                    # If the stack is empty, this bar extends all the way to index 0 (virtual start -1).
                    width = i
                else:
                    # Width is current index (i) minus the index of the bar to its left (stack[-1]) minus one.
                    width = i - stack[-1] - 1
                
                # 3. Calculate Area and Update Max
                current_area = height * width
                max_area = max(max_area, current_area)

            # Push the current index onto the stack
            stack.append(i)
            
        return max_area