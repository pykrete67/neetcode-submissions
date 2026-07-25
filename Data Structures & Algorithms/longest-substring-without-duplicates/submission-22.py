from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # since set is unordered, we need pointers to tell which element to remove

        my_set = set()
        l = 0
        maxx = 0

        for index, item in enumerate(s):
            if item not in my_set:
                my_set.add(item)
                maxx = max(maxx, (index-l+1))
            else:
                while item in my_set:
                    my_set.remove(s[l])
                    l += 1
                my_set.add(item)

                maxx = max(maxx, (index-l+1))

        return maxx

        # approach below is the correct approach but using deque it's O(N^2), so we need to use set instead

        # if not s:
        #     return 0
        # temp = deque()
        # maxx = 1

        # for n in s:

        #     if n not in temp:
        #         temp.append(n)
        #         maxx = max(maxx, len(temp))
        #     else:
        #         maxx = max(maxx, len(temp))
        #         temp.append(n)
        #         while temp: # this while loop is used to remove all elements up to the duplicate
        #             removed = temp.popleft()
        #             if removed == n:
        #                 break

        # print(temp)
        # return maxx


        