from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1

            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    
        return [ list(t) for t in ans]


if __name__ == "__main__":
    s = Solution()

    test = [-1,0,1,2,-1,-4]

    print(s.threeSum(test))
