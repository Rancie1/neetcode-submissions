class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0

        index = defaultdict(int)

        for right in range(len(s)):
            if s[right] in index:
                left = max(index[s[right]]+1, left)

            index[s[right]] = right
            ans = max(right-left+1,ans)

            
            
            

        return ans
        