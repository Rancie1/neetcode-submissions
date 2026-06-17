class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for s in strs:
            new = str(len(s)) + "#" + s
            ans.append(new)
        return "".join(ans)
        

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            wordLength = int(s[i:j])
            i = j + 1
            ans.append(s[i:j + wordLength + 1])
            i += wordLength
        return ans

            
