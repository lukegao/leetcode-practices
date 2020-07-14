
class Solution:
    def distinctSubseqII(self, S: str) -> int:
        dp = []
        length = len(S)
        chars = {}

        for i in range(length):
            dp.append(None)

        dp.append(0)

        total = 0
        for i in reversed(range(length)):
            accumu = 0

            if S[i] not in chars:
                chars[S[i]] = True
                accumu += 1

            for j in range(i+1, length):
                accumu += dp[j]

                if S[i] == S[j]:
                    break

            dp[i] = accumu

            total += dp[i]

        return total % (10**9 + 7)


if __name__ == '__main__':
    case1 = 'bebb'
    case2 = 'aba'
    case3 = 'abc'

    s = Solution()

    print(s.distinctSubseqII(case1))
    print(s.distinctSubseqII(case2))
    print(s.distinctSubseqII(case3))
