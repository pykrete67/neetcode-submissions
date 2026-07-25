class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_area = 0

        while l < r:
            area = (r-l)*(min(height[l], height[r]))
            max_area = max(area, max_area)
            # since moving pointer means we are closing in and area is only limited by the shorter line, we only need to move pointer to try to find a longer line on the side of the shorter line.
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area