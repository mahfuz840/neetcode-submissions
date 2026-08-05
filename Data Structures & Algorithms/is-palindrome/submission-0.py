class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            leftChar = s[left].lower()
            rightChar = s[right].lower()

            if not (leftChar >= 'a' and leftChar <= 'z') \
            and not (s[left] >= '0' and s[left] <= '9'):
                left += 1
                continue
            
            if not (rightChar >= 'a' and rightChar <= 'z') \
            and not (rightChar >= '0' and rightChar <= '9'):
                right -= 1
                continue
            
            if leftChar != rightChar:
                return False
            left += 1
            right -= 1
        
        return True