class Solution:
    
    def isSubset(self, a, b):
        from collections import Counter
    
        freq_a = Counter(a)
        
        for num in b:
            if freq_a.get(num, 0) == 0:
                return False
            freq_a[num] -= 1 
        
        return True

    
    
