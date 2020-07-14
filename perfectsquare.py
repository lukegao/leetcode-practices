
# Another solution is to use BFS.
# The root node is n, and we are trying to keep reduce a perfect square number from it each layer. 
# So the next layer nodes are {n - i**2 for i in range(1, int(n**0.5)+1)}. 
# And target leaf node is 0, indicates n is made up of a number of perfect square numbers and 
# depth is the least number of perfect square numbers.

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        d, q, nq = 1, {n}, set()
        while q:
            print(len(q))
            for node in q:
                for square in squares:
                    if node == square: return d
                    if node < square: break
                    nq.add(node-square)
            q, nq, d = nq, set(), d+1

if __name__ == '__main__':
    
    s = Solution()

    result = s.numSquares(6713)
    print(result)
