class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float("-inf")

        for i in range(n):
            curr = 0
            for j in range(i,n):
                curr += nums[j]
                ans = max(ans,curr)
            
        return ans




        