
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        index = 0

        while index < len(nums):
            if nums[index] != index+1:
                target = nums[index]-1

                nums[index] = 0
                print("Set {} to 0".format(index))
                print("Next target is {}".format(target))
                index += 1
                while nums[target] != target + 1:
                    temp = nums[target]
                    nums[target] = target + 1
                    print("Set {} to {}".format(target, target+1))
                    if temp == 0:
                        break
                    target = temp-1
                    print("Next target is {}".format(target))
            else:
                index += 1

        for i in range(len(nums)):
            if nums[i] == 0:
                result.append(i+1)
        return result


if __name__ == '__main__':
    s = Solution()

    test = [4, 3, 2, 7, 8, 2, 3, 1]

    r = s.findDisappearedNumbers(test)
    print(r)
