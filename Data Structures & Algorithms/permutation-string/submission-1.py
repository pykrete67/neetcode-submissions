class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #edge cases

        if len(s1) > len(s2):
            return False
        temp = {}
        temp2 = {}
        l = 0
        r = len(s1)

        # set up the first dict to check against the second one
        for n in s1:
            temp[n] = temp.get(n, 0) + 1

        # set up the second dict as window
        for n in s2[:len(s1)]: # only add the elements within the windows size
            temp2[n] = temp2.get(n, 0) + 1

        if temp2 == temp:
                return True

        # we solve this by comparing the 2 windows and adding and removing elements

        while r < len(s2):
            temp2[s2[r]] = temp2.get(s2[r], 0) + 1
            temp2[s2[l]] = temp2.get(s2[l], 0) - 1

            if temp2[s2[l]] == 0:
                del temp2[s2[l]]

            if temp2 == temp:
                return True
            
            l += 1
            r += 1

        return False


