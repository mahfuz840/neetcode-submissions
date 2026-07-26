class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroCount = 0

        for num in nums:
            if num != 0:
                prod *= num
            else:
                zeroCount += 1
        
        ans = []
        
        for num in nums:
            if num == 0:
                if zeroCount > 1:
                    ans.append(0)
                else:
                    ans.append(prod)
            elif zeroCount > 0:
                ans.append(0)
            else:
                ans.append(prod // num)
        
        return ans