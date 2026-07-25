from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        if not s:
            return 0

        temp = deque()
        maxx = 1
        prev = s[0]

        for n in s:

            if n == prev:
                temp.clear()

            if n not in temp:
                temp.append(n)
                maxx = max(maxx, len(temp))
                prev = n
            else:
                maxx = max(maxx, len(temp))
                first = temp.popleft()
                temp.append(n)
                prev = n

        return maxx


        