class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        end = len(matrix[0]) - 1

        for row in matrix:

            if target == row[0] or target == row[end]:
                return True

            if target > row[0] and target < row[end]:
                for col in row:
                    if target == col:
                        return True
                
                return False
        
        return False