class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for n in nums:
            if n not in dict:
                dict[n] = n
            else:
                return True
        return False

         