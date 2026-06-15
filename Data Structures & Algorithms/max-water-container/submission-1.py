class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            length = right - left
            height = min(heights[left],heights[right])
            area = length * height
            ans = max(ans,area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return ans
        