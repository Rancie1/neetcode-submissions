class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        stores = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in stores:
                streak += 1
                curr += 1
            ans = max(ans,streak)
        return ans

        