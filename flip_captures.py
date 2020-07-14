
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board:
            return []

        h, w = len(board), len(board[0])
        cache = {}

        def dfs(r, c, bd):

            if bd[r][c] == 'O':
                if r == 0 or r == h-1 or c == 0 or c == w-1:
                    return True
                else:
                    if (r, c) in cache:
                        return cache[r, c]

                    bd[r][c] = '#'
                    up = dfs(r-1, c, bd)
                    down = dfs(r+1, c, bd)
                    left = dfs(r, c-1, bd)
                    right = dfs(r, c+1, bd)
                    if up or down or left or right:
                        bd[r][c] = 'O'
                        cache[r, c] = True
                        return True
                    else:
                        bd[r][c] = 'O'
                        return False
            else:
                return False

        for i in range(h):
            for j in range(w):
                if not dfs(i, j, board):
                    board[i][j] = 'X'

        return


if __name__ == "__main__":
    s = Solution()
    test = [
        ["X", "X", "X", "X", "O", "X"],
        ["O", "X", "X", "O", "O", "X"],
        ["X", "O", "X", "O", "O", "O"],
        ["X", "O", "O", "O", "X", "O"],
        ["O", "O", "X", "X", "O", "X"],
        ["X", "O", "X", "O", "X", "X"]
    ]

    s.solve(test)

    for line in test:
        print(line)
