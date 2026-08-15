class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0
        right = rows * cols - 1

        while (left<=right):
            middle = (left + right) // 2
            """
            matrix is [3][4]
            rows = 3
            cols = 4
            left = 0
            right = 11
            middle = 5
            matrix[1][1]
            row = middle // cols
            col = middle % cols
            """
            row = middle // cols
            col = middle % cols 
            check = matrix[row][col]
            if check == target:
                return True
            elif check < target:
                left+=1
            elif check > target:
                right-=1
        return False