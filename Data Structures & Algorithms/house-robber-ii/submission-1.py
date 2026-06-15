class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dp(i,nums,memo):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(dp(i+1,nums,memo),dp(i+2,nums,memo)+nums[i])
            return memo[i]
        memo1 = {}
        memo2 = {}

        nums1 = nums[:len(nums)-1]
        nums2 = nums[1:len(nums)]

        ans1 = dp(0,nums1,memo1)
        ans2 = dp(0,nums2,memo2)

        return max(ans1,ans2)




            
        