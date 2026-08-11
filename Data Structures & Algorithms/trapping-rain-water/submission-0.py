class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [None] * n
        right_max = [None] * n
        left_max[0] = height[0]
        right_max[n-1] = height[n-1]

        for i, h in enumerate(height):
            if i == 0:
                continue
            
            left_max[i] = max(left_max[i-1], height[i])

        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1], height[i])
        
        area = 0
        for i, h in enumerate(height):
            area += min(left_max[i], right_max[i]) - height[i]
        
        return area
