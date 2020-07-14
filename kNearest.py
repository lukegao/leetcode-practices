
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        def findleftmostindex(arr, x):
            
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] >= x:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        
        index = findleftmostindex(arr, x)
        if index == 0:
            return arr[:k]
        if index == len(arr):
            return arr[k:]
        
        l, r = index, index
        while r - l < k:
            if l-1 >=0 and (r == len(arr) or (x-arr[l-1]) <= (arr[r]-x)):
                l -= 1
            elif r + 1 <= len(arr):
                r += 1


        return arr[l:r]


if __name__ == '__main__':
    s = Solution()

    test = [0,0,1,2,3,3,4,7,7,8]
    k = 8
    x = 5


    print(s.findClosestElements(test, k, x))