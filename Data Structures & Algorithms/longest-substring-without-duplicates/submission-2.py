class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        maxx = 0

        for n in s:
            if n.isalnum() == False:
                continue
            if n not in my_set:
                my_set.add(n)
            else:
                maxx = max(maxx, len(my_set))
                print(n)
                my_set.clear()
                my_set.add(n)
                continue

        return maxx