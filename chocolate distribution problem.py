class Solution:

    def findMinDiff(self, arr, M):
        if M == 0 or len(arr) == 0:
            return 0
        
        if M > len(arr):
            return -1
        
    
        arr.sort()
        
        min_diff = float('inf')
        
        for i in range(len(arr) - M + 1):
            diff = arr[i + M - 1] - arr[i]
            min_diff = min(min_diff, diff)
        
        return min_diff
