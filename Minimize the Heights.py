class Solution: 
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0
        arr.sort()
        
        ans = arr[-1] - arr[0]
        small = arr[0] + k
        big = arr[-1] - k
        
  
        if small > big:
            small, big = big, small
    
        for i in range(1, n - 1):
            subtract = arr[i] - k
            add = arr[i] + k
          
            if subtract < 0:
                continue
            minimum = min(small, subtract)
            maximum = max(big, add)
            
            ans = min(ans, maximum - minimum)
        
        return ans
