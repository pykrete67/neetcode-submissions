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
        high = len(self.temp[key])
        values = self.temp[key]
        result = ""
        # just normal binary search
        while low < high:
            middle = (low + high) // 2
            # we do [middle][1] because for middle, we are pointing to the middle list in the list of lists not the actual value yet, so we need [middle][1] to get the timestamp of hte list at the middle
            if values[middle][1] <= timestamp:
                # now, [middle][0] is the value of the middle list of the lists stored at key
                # we need to store the value first because if the val at the timestamp we are looking for isnt there, we need to get the most recent one before the timestamp that we are looking for. like if we want at timestamp 67 but it doesnt exist, we return the val at timestamp 66 and so on
                result = values[middle][0]
                low = middle + 1
            else:
                high = middle

        return result
        
        
