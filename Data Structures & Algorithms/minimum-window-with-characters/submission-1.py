class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        res = [-1,-1]
        resLen = float("inf")

        countT = defaultdict(int)
        window = defaultdict(int)

        
        for c in t:
            countT[c] += 1
            
        have = 0    
        need = len(countT)


        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l,r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        if resLen < float("inf"):
            return s[l:r+1]
        else:
            return ""

            

