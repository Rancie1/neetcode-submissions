class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(row,col):
            if row + col == 0:
                return 1

            if (row,col) in memo:
                return memo[(row,col)]

            

            if row == 0:
                ans = 1

            elif col == 0:
                ans = 1
            else:
                ans = dp(row-1,col) + dp(row,col-1)

            memo[(row,col)] = ans

            return ans
        memo = {}
        return dp(m-1,n-1)
        