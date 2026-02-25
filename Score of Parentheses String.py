class Solution:
    def scoreOfParentheses(self, s):
        stack = [0]  # base score
        
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:  # ch == ')'
                last = stack.pop()
                if last == 0:
                    stack[-1] += 1   # "()" case
                else:
                    stack[-1] += 2 * last  # "(A)" case
        
        return stack[0]
