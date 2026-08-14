class MinStack:

    def __init__(self):
        self.st = []
        self.minheap = []
        heapq.heapify(self.minheap)

    def push(self, val: int) -> None:
        self.st.append(val)
        heapq.heappush(self.minheap, val)

    def pop(self) -> None:
        self.st.pop()
        self.minheap = self.st[::]
        heapq.heapify(self.minheap)

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minheap[0]
