class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackk = []

        for n in tokens:
            if n == "+" or n == "-" or n == "*" or n == "/":
                if n == "+":
                    # cant just convert 13/5 to 2 if i used only int without converting to float first
                    result = int(float(stackk[-2]) + float(stackk[-1]))
                    if stackk:
                        stackk.pop(-1)
                    if stackk:
                        stackk.pop(-1)
                    stackk.append(str(result))
                elif n == "-":
                    result = int(float(stackk[-2]) - float(stackk[-1]))
                    if stackk:
                        stackk.pop(-1)
                    if stackk:
                        stackk.pop(-1)
                    stackk.append(str(result))
                elif n == "*":
                    result = int(float(stackk[-2]) * float(stackk[-1]))
                    if stackk:
                        stackk.pop(-1)
                    if stackk:
                        stackk.pop(-1)
                    stackk.append(str(result))
                elif n == "/":
                    result = int(float(stackk[-2]) / float(stackk[-1]))
                    if stackk:
                        stackk.pop(-1)
                    if stackk:
                        stackk.pop(-1)
                    stackk.append(str(result))

            else:
                stackk.append(n)
        
        return int(stackk[-1])