class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackk = []

        for n in tokens:
            if n == "+" or n == "-" or n == "*" or n == "/":
                if n == "+":
                    result = int(stackk[-2]) + int(stackk[-1])
                    stackk.pop(-1)
                    stackk.append(str(result))
                elif n == "-":
                    result = int(stackk[-2]) - int(stackk[-1])
                    stackk.pop(-1)
                    stackk.append(str(result))
                elif n == "*":
                    result = int(stackk[-2]) * int(stackk[-1])
                    stackk.pop(-1)
                    stackk.append(str(result))
                elif n == "/":
                    result = int(stackk[-2]) / int(stackk[-1])
                    stackk.pop(-1)
                    stackk.append(str(result))

            else:
                stackk.append(n)
        
        return int(stackk[-1])