class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = i
        
        for i, num in enumerate(nums):
            comp = target - num
            idx = dic.get(comp)
            if idx and idx != i:
                return [i, idx]
