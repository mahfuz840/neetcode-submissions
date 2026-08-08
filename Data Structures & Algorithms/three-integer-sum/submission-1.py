class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        uniq = set()

        nums.sort()

        for i, x in enumerate(nums):
            target = 0 - x
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sm = nums[j] + nums[k]
                if sm == target:
                    arr = [nums[i], nums[j], nums[k]]
                    uniq_str = f"{nums[i]}{nums[j]}{nums[k]}"
                    if uniq_str not in uniq:
                        ans.append(arr)
                        uniq.add(uniq_str)
                    k -= 1
                elif sm < target:
                    j += 1
                else:
                    k -= 1
        
        return ans

