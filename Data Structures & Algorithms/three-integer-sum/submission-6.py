class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        uniq = set()

        nums.sort()

        for i, x in enumerate(nums):
            if x > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - x
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sm = nums[j] + nums[k]
                if sm == target:
                    arr = [nums[i], nums[j], nums[k]]
                    if arr not in ans:
                        ans.append(arr)
                    k -= 1
                elif sm < target:
                    j += 1
                else:
                    k -= 1
        
        return ans

