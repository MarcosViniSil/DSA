#Link to problem: https://leetcode.com/problems/valid-sudoku/description/
#Time complexity: O(n^2)
#Space complexity: O(n)
                       
class Solution:
    def valid_sudoku(self,board:list[list[str]]) -> bool:
        
        row_count = {}
        column_count = {}
        grid_count = [{},{},{}]

        for i in range(len(board)):
            
            if i % 3 == 0:
                for counter in grid_count:
                    counter = {}
            
            for j in range(len(board[0])):
                if board[i][j] == "." or board[j][i] == ".":
                    continue

                if row_count.get(board[i][j]) is not None:
                    return False
                row_count[board[i][j]] = 1

                if column_count.get(board[j][i]) is not None:
                    return False
                column_count[board[j][i]] = 1

                if grid_count[j // 3].get(board[i][j]) is not None:
                    return False
                grid_count[j // 3][board[i][j]] = 1

            
            row_count = {}
            column_count = {}


        return True
                                        
solution = Solution()
print(solution.valid_sudoku(
[   
    ["5","3",".",".","7",".",".",".","."]
   ,["6",".",".","1","9","5",".",".","."]
   ,[".","9","8",".",".",".",".","6","."]
   ,["8",".",".",".","6",".",".",".","3"]
   ,["4",".",".","8",".","3",".",".","1"]
   ,["7",".",".",".","2",".",".",".","6"]
   ,[".","6",".",".",".",".","2","8","."]
   ,[".",".",".","4","1","9",".",".","5"]
   ,[".",".",".",".","8",".",".","7","9"]

]))

print(solution.valid_sudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
