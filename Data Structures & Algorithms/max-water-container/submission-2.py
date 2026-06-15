class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        ans = 0
        
        while left < right:
            height = min(heights[left],heights[right])
            curr_vol = (right-left) * height
            ans = max(curr_vol,ans)

            if heights[left] < heights[right]:
                left +=1
            else:
                right -= 1
        return ans

        