

class Solution:

    def decodeString(self, s: str) -> str:
        valstack = []
        numstack = []

        digits = '0123456789'

        numstr = ''
        for i in s:
            if i in digits:
                numstr = numstr + i
            else:
                if numstr:
                    d = int(numstr)
                    numstack.append(d)
                    numstr = ''

                if i != ']':
                    valstack.append(i)

                else:
                    substr = ''
                    while valstack and valstack[-1] != '[':
                        substr = valstack[-1] + substr 
                        valstack.pop()
                    if valstack:
                        valstack.pop()

                    if numstack:
                        substr = substr * numstack[-1]
                        numstack.pop()

                    valstack.append(substr)

        return ''.join(valstack)


if __name__ == '__main__':
    s = Solution()

    # test = "100[leetcode]"
    test = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    print(test)
    ans = s.decodeString(test)
    print(ans)
