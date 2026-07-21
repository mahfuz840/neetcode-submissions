class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in dic and dic[comp] != i:
                return [dic[comp], i]
            dic[num] = i
