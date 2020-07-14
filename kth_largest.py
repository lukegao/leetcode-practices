
from typing import List
import heapq


class Solution:
    def findKthLargest_alt(self, nums: List[int], k: int) -> int:

        result = heapq.nlargest(k, nums)

        return result[-1]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        pass


if __name__ == '__main__':
    s = Solution()

    case1 = [3, 2, 1, 5, 6, 4]
    case2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]

    print(s.findKthLargest_alt(case1, 2))
    print(s.findKthLargest_alt(case2, 4))
