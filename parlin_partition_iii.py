
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:

        def nParlin(string) -> int:
            count = 0
            l, r = 0, len(string)-1
            while l < r:
                if string[l] != string[r]:
                    count += 1
                l += 1
                r -= 1
            return count

        strlen = len(s)
        # par = [[False] * (strlen-i) for i in range(strlen)]
        par = {}

        for i in range(strlen):
            for j in range(i, strlen):
                par[i, j] = nParlin(s[i:j+1])

        def mincuts(start, string, K):
            choices = []
            if K == 1:
                return par[start, len(string)-1]

            for idx in range(start, len(string) - K + 1):
                choices.append(par[start, idx] + mincuts(idx+1, string, K-1))
            return 0 if not choices else min(choices)

        # dp = [[None] * (strlen-k) for i in range(k)]
        # dp[k-1][strlen-k-1] = 0

        # for i in range(k):
        #     for j in range(strlen-k-1, -1, -1):
        #         dp[i][j] = min([par[j][s] + dp[i-1][s+1] for s in range(j, strlen - k)])

        return mincuts(0, s, k)


if __name__ == "__main__":
    s = Solution()
    test = ('aabbc', 3)
    print(s.palindromePartition(test[0], test[1]))
