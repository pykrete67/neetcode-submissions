from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        if not s:
            return 0

        temp = deque()
        maxx = 1

        for n in s:

            if n not in temp:
                temp.append(n)
                maxx = max(maxx, len(temp))
            else:
                maxx = max(maxx, len(temp))
                first = temp.popleft()

        return maxx


        