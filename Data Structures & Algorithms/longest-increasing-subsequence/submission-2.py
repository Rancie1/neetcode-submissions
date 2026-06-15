class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        
        
        for i in range(1,n):
            ans = 1
            for j in range(0,i):
                if nums[j] < nums[i]:
                    ans = max(ans, dp[j] + 1)
            dp[i] = ans

        res = 1
        for i in range(n):
            res = max(dp[i], res)

        return res