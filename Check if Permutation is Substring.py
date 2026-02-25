# User function Template for python3
class Solution:
    def search(self, txt, pat):
        from collections import Counter
        
        n, m = len(txt), len(pat)
        if m > n:
            return False
        
        pat_count = Counter(pat)
        window_count = Counter(txt[:m])
        
        if window_count == pat_count:
            return True
        
        for i in range(m, n):
            # Add new character
            window_count[txt[i]] += 1
            
            # Remove old character
            left_char = txt[i - m]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
            
            if window_count == pat_count:
                return True
        
        return False
