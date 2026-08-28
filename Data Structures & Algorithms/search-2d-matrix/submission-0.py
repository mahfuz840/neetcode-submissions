class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = m*n
        start = 0
        end = l-1

        while start <= end and start >=0 and end < l:
            temp = (start+end) // 2
            midx = temp // n
            midy = temp % n
            if matrix[midx][midy] == target:
                return True
            elif matrix[midx][midy] > target:
                end = temp - 1
            else:
                start = temp + 1
        
        return False