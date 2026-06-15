class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        def dp(i):
            if i == 0:
                return 1
            if i in memo:
                return memo[i]

            ans = 1
            for j in range(0,i):
                if nums[j] < nums[i]:
                    ans = max(dp(j)+1,ans)

            memo[i] = ans
            return ans

        memo = {}
        res = 0
        for i in range(len(nums)):
            res = max(res, dp(i))
        return res

        