class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashed = set(nums)
        length = {}
        longest = 0

        nums.sort()

        for num in nums:
            prevLength = length.get(num-1, 0)
            currLength = prevLength + 1
            length[num] = currLength
            longest = max(longest, currLength)
        
        return longest
