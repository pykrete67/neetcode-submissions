class MinStack:
    # approach: create another stack to keep track of the lowest value
    def __init__(self):
        self.mainstack = []
        self.minstack = []

        

    def push(self, val: int) -> None:
        self.mainstack.append(val)
        if self.minstack:
            self.minstack.append(min(self.minstack[-1], val))
        else:
            self.minstack.append(val)
        
    def pop(self) -> None:
        self.mainstack.pop(-1)
        self.minstack.pop(-1)
        

    def top(self) -> int:
        return self.mainstack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
