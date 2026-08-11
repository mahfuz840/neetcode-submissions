class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            left_val = heights[left]
            right_val = heights[right]
            x = min(left_val, right_val)
            ans = max(ans, x * (right-left))

            if left_val < right_val:
                left += 1
            else:
                right -= 1

        return ans