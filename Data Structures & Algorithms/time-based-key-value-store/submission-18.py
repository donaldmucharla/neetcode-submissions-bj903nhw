class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.store:
            return ""

        values = self.store[key]
        l = 0
        r = len(values)-1
        res = ""
        while l <= r:
            k = (l+r) //2

            if values[k][1] <= timestamp:
                res = values[k][0]
                l = k+1
            else:
                r = k - 1
        
        return res

