class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        maxx = 1
        temp = 0

        if not s:
            return 0

        for index in range(len(s)):
            if s[index] not in my_set:
                my_set.add(s[index])
                maxx = max(maxx, len(my_set))
            else:
                if s[index-1] != s[index]:
                    temp = s[index-1]
                maxx = max(maxx, len(my_set))
                my_set.clear()
                if temp != 0:
                    my_set.add(temp)
                my_set.add(s[index])

        return maxx