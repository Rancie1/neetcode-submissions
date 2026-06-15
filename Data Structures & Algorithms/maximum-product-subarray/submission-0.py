class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = ans = nums[0]

        for i in range(1,len(nums)):
            x = nums[i]

            prev_max = max_prod

            max_prod = max(x, x * max_prod, x * min_prod)
            min_prod = min(x, x * prev_max, x * min_prod)

            ans = max(ans, max_prod)

        return ans
        