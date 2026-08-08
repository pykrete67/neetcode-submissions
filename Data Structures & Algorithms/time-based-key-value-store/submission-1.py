class TimeMap:

    def __init__(self):
        self.temp = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.temp:
            self.temp[key] = []
        self.temp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        # edge case
        if key not in self.temp:
            return ""
        low = 0
        high = len(self.temp[key]) - 1
        values = self.temp[key]
        result = ""

        while low <= high:
            middle = (low + high) // 2

            if values[middle][1] <= timestamp:
                result = values[middle][0]
                low = middle + 1
            else:
                high = middle - 1

        return result
        
        
