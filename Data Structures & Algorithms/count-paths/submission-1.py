class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(i,j):
            if i == 0 or j == 0:
                return 1

            if (i,j) in memo:
                return memo[(i,j)]

            ans = dfs(i-1,j) + dfs(i,j-1)

            memo[(i,j)] = ans
            return ans  

        memo = {}

        return dfs(m-1,n-1)
        