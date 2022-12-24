'''
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/769/

Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.

'''
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        # Check no duplicate in row
        for r in range(N):
            row = [c for c in board[r] if c != "."]
            if len(row) != len(set(row)): return False
        
        # Check no duplicates in column
        for c in range(N):
            col = [board[r][c] for r in range(N) if board[r][c] != "."]
            if len(col) != len(set(col)): return False

        # Check no duplicate in box
        box = []
        
        # Create combinations to define a box
        count = 0
        box_arr = []
        arr_comb = []
        for i in range(N):
            arr_comb.append(i)
            count += 1
            if count == 3:
                box_arr.append(arr_comb)
                arr_comb = []
                count = 0
        # print(box_arr)

        for r in box_arr:
            for c in box_arr:
                for i in r:
                    for j in c:
                        # print(i, j)
                        if board[i][j]!= ".": box.append(board[i][j])
                # print("Box Done")
                if len(box) != len(set(box)): return False
                box = []
        
        return True


s = Solution()
board1 = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

out = s.isValidSudoku(board1)
print(f'{out=}')
