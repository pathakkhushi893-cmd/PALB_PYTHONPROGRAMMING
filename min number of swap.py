class Solution:
    def minSwaps(self, s1, s2):
        # If lengths are different, not possible
        if len(s1) != len(s2):
            return -1
        
        # Count mismatched positions
        xy = 0  # s1[i] = '0' and s2[i] = '1'
        yx = 0  
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == '0' and s2[i] == '1':
                    xy += 1
                else:  # s1[i] == '1' and s2[i] == '0'
                    yx += 1
        
        # If total mismatches are odd, impossible
        if (xy + yx) % 2 != 0:
            return -1
        
        return xy // 2 + yx // 2 + (xy % 2) * 2
