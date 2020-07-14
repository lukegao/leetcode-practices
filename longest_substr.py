

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i, j = 0, 0
        ans = 0
        
        while i < len(s):
            bag = set()
            j = i
            while j < len(s) and s[j] not in bag:
                bag.add(s[j])
                j += 1
            ans = max(ans, len(bag))
            i = j

        return ans


if __name__ == '__main__':
    s = Solution()

    test = 'dvdf'

    print(s.lengthOfLongestSubstring(test))