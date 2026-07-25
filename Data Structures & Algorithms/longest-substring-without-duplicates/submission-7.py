class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        maxx = 1

        if not s:
            return 0

        for n in s:
            if n not in my_set:
                my_set.add(n)
                maxx = max(maxx, len(my_set))
            else:
                maxx = max(maxx, len(my_set))
                my_set.clear()
                my_set.add(n)
                # continue

        return maxx