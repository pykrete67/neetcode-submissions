class Solution:
    def isValid(self, s: str) -> bool:
        # edge case

        if len(s) % 2 != 0:
            return False

        halfway = len(s) / 2
        index = 0

        stackk = []
        brackets = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        for n in s:
            if n == ")" and "(" not in stackk:
                return False
            if n == "]" and "[" not in stackk:
                return False
            if n == "}" and "{" not in stackk:
                return False
            if n == "(" or n == "[" or n == "{":
                stackk.append(n)
            else:
                if stackk[-1] == brackets[n]:
                    temp = stackk.pop(-1)
                else:
                    return False
                

        if not stackk: # if empty, return Talse
            return True