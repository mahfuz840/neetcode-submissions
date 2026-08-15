class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        monotonic = []

        for idx, temp in enumerate(temperatures):
            while monotonic and monotonic[-1][0] < temp:
                top = monotonic.pop()
                ans[top[1]] = idx - top[1]
            monotonic.append((temp, idx))
        
        return ans