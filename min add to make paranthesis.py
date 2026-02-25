class Solution:
    def minParentheses(self, s):
        balance = 0   # counts unmatched '('
        insertions = 0  # counts needed '(' for unmatched ')'
        
        for ch in s:
            if ch == '(':
                balance += 1
            else:  # ch == ')'
                if balance > 0:
                    balance -= 1
                else:
                    insertions += 1
        
        # balance represents unmatched '('
        return insertions + balance
