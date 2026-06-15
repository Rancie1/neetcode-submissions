class Solution:
    def numDecodings(self, s: str) -> int:
        def dp(i):
            if i == 0:
                return 1

            if i in memo:
                return memo[i]

            ans = 0

            if s[i-1] != '0':
                ans += dp(i-1) 

            if i >= 2 and 10 <= int(s[i-2:i]) < 27:
                ans += dp(i-2)
        

            memo[i] = ans
            return ans

        memo = {}
        return dp(len(s))



            

        