from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Handle the edge case of an empty array
        if not nums:
            return 0
        
        # Step 1: Store all unique numbers in a set for O(1) average time lookup.
        num_set = set(nums)
        longest_streak = 0
        
        # Step 2: Iterate through the unique numbers.
        for x in num_set:
            # Optimization Check: We only want to start counting if 'x' is the start of a sequence.
            # If x - 1 exists, we skip it because it will be counted when the outer loop reaches x-1.
            if (x - 1) not in num_set:
                # x is the potential start of a new consecutive sequence
                current_num = x
                current_streak = 1
                
                # Step 3: Count the length of the current sequence using the while loop
                # This loop runs until we hit a number that is not in the set.
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Step 4: Update the global longest streak found so far
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak

# Example Usage:
# sol = Solution()
# print(sol.longestConsecutive([2, 20, 4, 10, 3, 4, 5])) # Output: 4 ([2, 3, 4, 5])
# print(sol.longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1])) # Output: 7 (The sequence is [0] to [6], assuming the prompt means length 7 from 0 to 6)
