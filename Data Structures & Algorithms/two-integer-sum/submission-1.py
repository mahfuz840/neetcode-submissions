class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            if not dic.get(num):
                dic[num] = set([i])
            else:
                dic[num].add(i)
        
        sorted_nums = sorted(nums)

        left = 0
        right = len(nums) - 1
        ans = []
        while left < right:
            curr_sum = sorted_nums[left] + sorted_nums[right]
            if curr_sum < target:
                left = left + 1
            elif curr_sum > target:
                right = right - 1
            elif curr_sum == target:
                ans = [sorted_nums[left], sorted_nums[right]]
                break

        return sorted([dic[ans[0]].pop(), dic[ans[1]].pop()])