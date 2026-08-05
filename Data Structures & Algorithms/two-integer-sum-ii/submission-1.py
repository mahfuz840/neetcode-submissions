class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left = i
            right = len(numbers) - 1
            other = target - numbers[i]

            while left <= right:
                mid = (left + right + 1) // 2

                if numbers[mid] == other:
                    return [i + 1, mid + 1]
                elif numbers[mid] < other:
                    left = mid + 1
                else:
                    right = mid - 1

            