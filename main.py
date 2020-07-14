
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        table = {}
        maxlen = 1

        for i in nums:
            table[i] = True

        for key, flag in table.items():
            if not flag:
                continue

            sublen = 1
            cursor = key
            table[cursor] = False

            while True:
                if cursor-1 in table and table[cursor-1]:
                    sublen += 1
                    cursor -= 1
                    table[cursor] = False
                else:
                    break

            cursor = key
            while True:
                if cursor+1 in table and table[cursor+1]:
                    sublen += 1
                    cursor += 1
                    table[cursor] = False
                else:
                    break
            if maxlen < sublen:
                maxlen = sublen
        return maxlen


if __name__ == '__main__':
    s = Solution()
    case1 = [0, -1]
    case2 = [100, 2, 3, 4, 99]
    case3 = [2147483646, -2147483647, 0, 2,
             2147483644, -2147483645, 2147483645]
    print(s.longestConsecutive(case1))
    print(s.longestConsecutive(case2))
    print(s.longestConsecutive(case3))
