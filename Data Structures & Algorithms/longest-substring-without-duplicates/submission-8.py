class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        maxx = 1

        if not s:
            return 0

        for index in range(len(s)):
            if s[index] not in my_set:
                my_set.add(s[index])
                maxx = max(maxx, len(my_set))
            else:
                maxx = max(maxx, len(my_set))
                my_set.clear()
                my_set.add(s[index])
                index -= 1
                # continue

        return maxx