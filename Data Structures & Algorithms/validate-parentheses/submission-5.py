class Solution:
    def isValid(self, s: str) -> bool:
        # edge case

        if len(s) % 2 != 0:
            return False

        stackk = []
        brackets = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        for n in s:
            # commenting these parts out, it makes the solution O(N^2)
            # if n == ")" and "(" not in stackk:
            #     return False
            # if n == "]" and "[" not in stackk:
            #     return False
            # if n == "}" and "{" not in stackk:
            #     return False
            if n == "(" or n == "[" or n == "{":
                stackk.append(n)
            else:
                # just add this check to make it O(N)
                if not stackk:
                    return False
                if stackk[-1] == brackets[n]:
                    temp = stackk.pop(-1)
                else:
                    return False
                

        if stackk: # if not empty, return False
            return False
        else:
            return True