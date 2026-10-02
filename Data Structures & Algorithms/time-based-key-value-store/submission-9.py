class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            tup = (timestamp, value)
            arr = [tup]
            self.dict[key] = arr
        else:
            heapq.heappush(self.dict.get(key), (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        tups = self.dict.get(key)
        if tups is None:
            return ""
        
        n = len(tups)
        if n==1:
            return tups[0][1] if tups[0][0] <= timestamp else ""

        left = 0
        right = n-1
        
        while left < right:
            mid = (left+right+1) // 2
            if tups[mid][0] == timestamp:
                return tups[mid][1]
            elif tups[mid][0] > timestamp:
                right = mid-1
            else:
                left = mid
        
        if tups[left][0] <= timestamp:
            return tups[left][1]
        
        return ""

