class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                if nums[mid] > nums[right]:
                    left = mid+1
                elif target > nums[right]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid] < nums[left]:
                    right = mid-1
                elif target >= nums[left]:
                    right = mid-1
                else:
                    left = mid+1
        
        return -1