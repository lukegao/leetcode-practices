from typing import str


class Solution:

    def longestPalindrome(self, s: str) -> int:

        def helper(string):
            lens = len(string)
            if lens < 2:
                return lens

            l, r = 0, lens-1
            if string[l] == string[r]:
                return helper(string[l+1:r]) + 2
            else:
                return max(helper(string[l+1:lens]), helper(string[l:lens-1]))

        return helper(s)


if __name__ == "__main__":
    pass