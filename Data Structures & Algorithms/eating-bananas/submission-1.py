class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = -1
        for pile in piles:
            mx = max(mx, pile)

        start = 1
        end = mx

        while start < end and start >= 1 and end <= mx:
            mid = (start+end) // 2
            totalHours = 0
            for pile in piles:
                hoursToEat = math.ceil(pile / mid)
                totalHours += hoursToEat
                if totalHours > h:
                    break
            print(mid, totalHours)
            if totalHours <= h:
                end = mid
            elif totalHours > h:
                start = mid + 1
        
        return (start+end) // 2