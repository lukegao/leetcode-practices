from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        row, col = amount + 1, len(coins) + 1

        dp = [[0]*col for i in range(row)]
        dp[0] = [1] * col

        for r in range(1, row):
            for c in range(1, col):
                dp[r][c] = dp[r][c-1]
                if r >= coins[c-1]:
                    dp[r][c] += dp[r-coins[c-1]][c]

        for r in range(row):
            print(dp[r])
        return dp[amount][col-1]


if __name__ == "__main__":
    s = Solution()

    # test = (5, [1, 2, 5])
    test = (500, [3, 5, 7, 8, 9, 10, 11])

    print(s.change(test[0], test[1]))
