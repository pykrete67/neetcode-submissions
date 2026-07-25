class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left = 0           # Left pointer starts at the beginning
        right = len(height) - 1 # Right pointer starts at the end
        
        max_left = 0       # Maximum height encountered from the left up to 'left'
        max_right = 0      # Maximum
