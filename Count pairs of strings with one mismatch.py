class Solution:
    def countPairs(self, arr):
        n = len(arr)
        if n < 2:
            return 0
        
        m = len(arr[0])  # length of each string
        count = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                diff = 0
                for k in range(m):
                    if arr[i][k] != arr[j][k]:
                        diff += 1
                        if diff > 1:
                            break
                if diff == 1:
                    count += 1
        
        return count
