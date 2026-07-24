from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the maximum element in a sliding window of size k using a monotonic deque.
        Time Complexity: O(N)
        Space Complexity: O(k)
        """
        if not nums or k == 0:
            return []

        # Deque stores indices, maintaining values in decreasing order (monotonic).
        dq = deque()
        result = []
        n = len(nums)

        for i in range(n):
            
            # Step 1: Maintain Monotonicity (Clean up from the back)
            # If the current element nums[i] is greater than or equal to 
            # the value at the index at the back of the deque, that old index 
            # can never be the maximum because nums[i] is larger and comes later.
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            
            # Step 2: Add current element's index
            dq.append(i)
            
            # Step 3: Manage Window Size (Clean up from the front)
            # The window starts at i - k + 1. If the index at the front is less than this, it's out of bounds.
            if dq[0] <= i - k:
                dq.popleft()
            
            # Step 4: Record Result
            # We only start recording results once the window size reaches k (i >= k - 1).
            if i >= k - 1:
                # The maximum element is always represented by the index at the front of the deque.
                result.append(nums[dq[0]])
        
        return result

# Example usage (for testing):
# sol = Solution()
# nums = [1, 2, 1, 0, 4, 2, 6]
# k = 3
# print(sol.maxSlidingWindow(nums, k)) # Expected: [2, 2, 4, 4, 6]

# nums2 = [9, 11]
# k2 = 2
# print(sol.maxSlidingWindow(nums2, k2)) # Expected: [11]
