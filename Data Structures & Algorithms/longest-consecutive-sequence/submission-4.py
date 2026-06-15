class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ans = 0
    
        numSet = set(nums)

        for num in numSet:
            if (num - 1) not in numSet:
                streak = 1
            
                while num + streak in numSet:
                    streak += 1

                ans = max(ans,streak)
        return ans

        