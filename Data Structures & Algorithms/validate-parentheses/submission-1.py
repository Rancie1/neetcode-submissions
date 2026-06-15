class Solution:
    def isValid(self, s: str) -> bool:
        matches = {"[":"]","(":")","{":"}"}
        stack = []

        for c in s:
            if c in matches:
                stack.append(c)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if matches[prev] != c:
                    return False
        return not stack
        