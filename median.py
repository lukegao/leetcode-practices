
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        def helper(k, lo1, hi1, nums1, lo2, hi2, nums2):
            print(k, nums1[lo1:hi1], nums2[lo2:hi2])
            if lo1 >= hi1:
                return nums2[lo2 + k]
            if lo2 >= hi2:
                return nums1[lo1 + k]

            mid1 = (lo1 + hi1) // 2
            mid2 = (lo2 + hi2) // 2

            m1, m2 = nums1[mid1], nums2[mid2]

            if (mid1 - lo1) + (mid2 - lo2) < k:
                if m1 < m2:
                    return helper(k - (mid1 - lo1 + 1), mid1+1, hi1, nums1, lo2, hi2, nums2)
                else:
                    return helper(k - (mid2 - lo2 + 1), lo1, hi1, nums1, mid2+1, hi2, nums2)
            else:
                if m1 < m2:
                    return helper(k, lo1, hi1, nums1, lo2, mid2, nums2)
                else:
                    return helper(k, lo1, mid1, nums1, lo2, hi2, nums2)

        if (m+n) % 2 == 0:
            return (helper((m+n) // 2, 0, m, nums1, 0, n, nums2) + helper((m+n) // 2 - 1, 0, m, nums1, 0, n, nums2)) / 2
        else:
            return helper((m+n) // 2, 0, m, nums1, 0, n, nums2)


def kth(a, b, k):
    print(k, a, b)
    if not a:
        return b[k]
    if not b:
        return a[k]
    ia, ib = len(a) // 2, len(b) // 2
    ma, mb = a[ia], b[ib]

    # when k is bigger than the sum of a and b's median indices
    if ia + ib < k:
        # if a's median is bigger than b's, b's first half doesn't include k
        if ma > mb:
            return kth(a, b[ib + 1:], k - ib - 1)
        else:
            return kth(a[ia + 1:], b, k - ia - 1)
    # when k is smaller than the sum of a and b's indices
    else:
        # if a's median is bigger than b's, a's second half doesn't include k
        if ma > mb:
            return kth(a[:ia], b, k)
        else:
            return kth(a, b[:ib], k)


if __name__ == '__main__':
    s = Solution()

    test1 = [1, 2, 3]
    test2 = [1, 2, 2]

    print(s.findMedianSortedArrays(test1, test2))
    print(kth(test2, test1, 2))
