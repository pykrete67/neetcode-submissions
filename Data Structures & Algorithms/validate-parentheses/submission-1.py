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
                

        if stackk: # if not empty, return False
            return False
        else:
            return True