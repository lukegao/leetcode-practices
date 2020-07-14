
from typing import List



class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        candidates = [str(i) for i in range(1, 10)]
        
        def get_valid(row, col):
            s1 = set(i for i in board[row] if i != '.')
            s2 = set(j for j in (i[col] for i in board) if j != '.')

            rs = (row // 3)*3
            re = rs + 3
            cs = (col // 3)*3
            ce = cs + 3
            
            s3 = set(board[i][j] for i in range(rs, re) for j in range(cs, ce) if board[i][j] != '.')

            return set(candidates) - s1 - s2 - s3
        
        def place(t, row, col):
            board[row][col] = t
        
        def remove(row, col):
            board[row][col] = '.'

        def nextcell(row, col):
            if row + 1 == n and col +1 ==n:
                return None
            elif col + 1 == n:
                return row+1, 0
            else:
                return row, col+1

        def backtrack(row, col):
            if board[row][col] != '.' and row+1 == n and col+1 == n:
                return True

            if board[row][col] == '.':
                numbers = get_valid(row, col)
                for num in numbers:
                    place(num, row, col)
                    cell = nextcell(row, col)
                    if not cell:
                        return True
                    ans = backtrack(cell[0], cell[1])
                    if ans:
                        return ans
                    remove(row, col)
                return False
            else:
                cell = nextcell(row, col)
                if not cell:
                    return True
                ans = backtrack(cell[0], cell[1])
                return ans

        
        # def backtrack0(row, col):
        #     if board[row][col] == '.':
        #         candi = get_valid(row, col)
        #         for c in candi:
        #             place(c, row, col)
        #             if row+1 == n and col+1 == n:
        #                 return True
        #             elif col+1 == n:
        #                 if backtrack(row+1, 0):
        #                     return True
        #             else:
        #                 if backtrack(row, col+1):
        #                     return True
        #             remove(row, col)
        #     else:
        #         if row+1 == n and col+1 == n:
        #             print("return with ", board[row])
        #             return True
        #         elif col+1 == n:
        #             if backtrack(row+1, 0):
        #                 return True
        #         else:
        #             if backtrack(row, col+1):
        #                 return True

        return backtrack(0, 0)


if __name__ == '__main__':
    s = Solution()

    test = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    # test = [
    # ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
    # ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
    # ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    # ['8', '5', '9', '7', '6', '1', '4', '2', '3'],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

    s.solveSudoku(test)
    for l in test:
        print(l)
