import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 0
        high = max(piles)
        lowest = max(piles)

        while low < high:
            middle = (low + high) // 2
            count = 0

            for n in piles:
                count += math.ceil(n/middle)

            print(count)
            
            if count <= h:
                lowest = middle
                high = middle
            else:
                low = middle + 1

        return lowest