class Solution:
    def maxSubseq(self, s, k):
        stack = []
        remove = k
        
        for ch in s:
            # Remove smaller characters if possible
            while stack and remove > 0 and stack[-1] < ch:
                stack.pop()
                remove -= 1
            stack.append(ch)
        
        # If still removals left, remove from end
        while remove > 0:
            stack.pop()
            remove -= 1
        
        return "".join(stack)
