from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        max_count = 0
        count = defaultdict(int)


        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count,count[s[right]])

            while (right-left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            ans = max(right-left+ 1, ans)
        return ans


            


        