class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        print(s, s[::-1])
        if not s or len(s) == 1:
            return s
        j = 0
        for i in reversed(range(len(s))):
            # print(i, j, s[i], s[j])
            if s[i] == s[j]:
                j += 1
        print(j, s[::-1][:len(s)-j], s[j-len(s):])
        return s[::-1][:len(s)-j] + self.shortestPalindrome(s[:j-len(s)]) + s[j-len(s):] 


if __name__ == '__main__':
    
    s = Solution()

    # test ='adfaa'
    test2 = 'dedcba'
    # test3 = 'abc'

    # print(s.shortestPalindrome(test))
    print(s.shortestPalindrome(test2))
    # print(s.shortestPalindrome(test3))