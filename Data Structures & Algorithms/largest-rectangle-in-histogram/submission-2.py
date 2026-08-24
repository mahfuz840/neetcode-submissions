class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        leftMost = [-1] * len(heights)
        rightMost = [len(heights)] * len(heights)

        stack = []

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)
        
        for i in range(len(heights)):
            leftMost[i] += 1
            rightMost[i] -= 1
            ans = max(ans, heights[i] * (rightMost[i] - leftMost[i] + 1))
        
        return ans
        
