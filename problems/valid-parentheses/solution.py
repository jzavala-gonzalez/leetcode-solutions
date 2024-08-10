class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = list()
        open_to_close = {
            '(': ')', '{':'}', '[':']'
        }
        for c in s:
            # c is a new opening parenthesis
            if c in open_to_close:
                open_stack.append(c)

            # c is a closing parenthesis
            elif open_stack and (open_to_close[open_stack.pop()] == c):
                continue
            else:
                return False
        
        return len(open_stack) == 0