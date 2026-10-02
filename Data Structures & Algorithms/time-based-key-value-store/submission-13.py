class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []

        self.dict.get(key).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        tups = self.dict.get(key)
        if tups is None:
            return ""
        
        n = len(tups)
        left = 0
        right = n-1
        
        while left < right:
            mid = (left+right+1) // 2
            if tups[mid][0] <= timestamp:
                left = mid
            else:
                right = mid - 1
        
        if tups[left][0] <= timestamp:
            return tups[left][1]
        
        return ""

