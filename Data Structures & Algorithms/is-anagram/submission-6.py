class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = defaultdict(int)
        countT = defaultdict(int)

        for c in s:
            countS[c] += 1
        
        for c in t:
            countT[c] += 1
        
        if len(countT) > len(countS):
            longer = countT
            shorter = countS
        else:
            longer = countS
            shorter = countT

        for key in longer:
            if longer[key] != shorter[key]:
                return False
        return True
        