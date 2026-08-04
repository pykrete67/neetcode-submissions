import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        lowest = max(piles)

        # dont need the edge case anymore if we set low = 1
        # if len(piles) == 1:
        #     return math.ceil(piles[-1]/h)

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