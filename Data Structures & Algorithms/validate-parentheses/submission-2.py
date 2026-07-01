class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        string = {')':'(',']':'[','}':'{'}
        valid = "({["
        for item in s:
            if item in valid:
                stack.append(item)
            elif not stack or stack.pop() != string[item]:
                return False
        return len(stack) == 0
        