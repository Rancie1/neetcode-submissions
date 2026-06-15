class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26

        for c in s:
            count[ord(c)-ord("a")] += 1
        for c in t:
            count[ord(c)-ord("a")] -= 1
        
        for char in count:
            if char != 0:
                return False
        return True