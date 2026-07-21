class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_list = set(nums)

        return len(nums) != len(unique_list)