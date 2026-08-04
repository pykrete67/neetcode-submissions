import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 0
        high = max(piles)
        lowest = max(piles)
        if len(piles) == 1:
            return (piles[-1] - h)+1

        while low < high:
            middle = (low + high) // 2
            count = 0

            for n in piles:
                count += math.ceil(n/middle)
            
            if count <= h:
                lowest = middle
                high = middle
            else:
                low = middle + 1

        return lowest