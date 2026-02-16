class Solution:
        
    def minSwap(self, arr, k): 
        n = len(arr)
        
        good = 0
        for num in arr:
            if num <= k:
                good += 1
        
        if good == 0 or good == n:
            return 0
        
        bad = 0
        for i in range(good):
            if arr[i] > k:
                bad += 1
        
        ans = bad
        

        for i in range(good, n):
            
            if arr[i - good] > k:
                bad -= 1
                
            
            if arr[i] > k:
                bad += 1
                
            ans = min(ans, bad)
        
        return ans


