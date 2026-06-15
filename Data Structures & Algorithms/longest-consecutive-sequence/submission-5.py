class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        numSet = set(nums)

        for num in nums:
            streak = 1
            curr = num + 1
            while curr in numSet:
                curr += 1
                streak += 1
            ans = max(streak,ans)
        return ans

        