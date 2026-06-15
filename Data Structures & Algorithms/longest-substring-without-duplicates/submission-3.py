class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = left = 0
        count = defaultdict(int)

        for right in range(len(s)):
            if s[right] in count:
                left = max(left,count[s[right]] + 1)
            
            count[s[right]] = right
            ans = max(ans, right - left + 1)

        return ans
        

        