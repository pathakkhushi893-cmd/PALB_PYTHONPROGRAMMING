from bisect import bisect_right

class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        min_val = min(row[0] for row in mat)
        max_val = max(row[-1] for row in mat)
        
        desired = (n * m) // 2 
        
        while min_val < max_val:
            mid = (min_val + max_val) // 2
            
            count = 0
            for row in mat:
                count += bisect_right(row, mid)
            
            if count <= desired:
                min_val = mid + 1
            else:
                max_val = mid
        
        return min_val
