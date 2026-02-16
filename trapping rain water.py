class Solution:
    def maxWater(self, arr):
        n = len(arr)
        if n <= 2:
            return 0  
        
        left, right = 0, n - 1
        left_max, right_max = arr[left], arr[right]
        water = 0
        
        while left < right:
            if arr[left] < arr[right]:
                left += 1
                left_max = max(left_max, arr[left])
                water += max(0, left_max - arr[left])
            else:
                right -= 1
                right_max = max(right_max, arr[right])
                water += max(0, right_max - arr[right])
        
        return water
