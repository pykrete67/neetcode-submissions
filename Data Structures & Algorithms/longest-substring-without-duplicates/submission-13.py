from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        temp = deque()
        maxx = 1

        for n in s:

            if n not in temp:
                temp.append(n)
            else:
                maxx = max(maxx, len(temp))
                first = temp.popleft()

        return maxx


        