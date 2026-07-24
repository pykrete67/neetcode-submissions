class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        l = 0
        r = len(s) - 1
        #print(s[r])
        while l < r:
            if s[l].isalnum() != True:
                l += 1
                continue
            if s[r].isalnum() != True:
                r -= 1
                print(s[r])
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
            
            
        