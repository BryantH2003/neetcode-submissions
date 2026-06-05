class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        cols = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        square = [[[],[],[]], [[],[],[]], [[],[],[]]]

        for row in range(9): 
            for col in range(9): 
                if board[row][col] == ".":
                    continue

                if board[row][col] in rows[row]:
                    return False
                else:
                    rows[row].append(board[row][col])

                if board[row][col] in cols[col]:
                    return False
                else:
                    cols[col].append(board[row][col])
                
                if board[row][col] in square[row//3][col//3]:
                    return False
                else:
                    square[row//3][col//3].append(board[row][col])
        
        print("rows:", rows)
        print("cols:", cols)
        print(square)
        return True
