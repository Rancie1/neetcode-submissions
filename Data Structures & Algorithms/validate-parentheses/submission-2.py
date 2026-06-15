class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {"(":")","[":"]","{":"}"}

        for c in s:
            if c in matches:
                stack.append(c)
            else:
                if stack:
                    other = stack.pop()
                    if matches[other] != c:
                        return False
                else:
                    return False
        return not stack

        