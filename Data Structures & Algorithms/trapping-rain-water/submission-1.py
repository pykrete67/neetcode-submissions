from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left = 0           
        right = len(height) - 1 
        
        max_left = 0       
        max_right = 0      
        total_water = 0    

        while left < right:
            if height[left] < height[right]:
                # Process the left side (limited by max_left)
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    water = max_left - height[left]
                    total_water += water
                
                left += 1
            else:
                # Process the right side (limited by max_right)
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    water = max_right - height[right]
                    total_water += water
                
                right -= 1
                
        return total_water
