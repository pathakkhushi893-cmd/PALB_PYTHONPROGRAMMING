class Solution:
    def rotate(self, arr):
        n = len(arr)
        
        if n <= 1:
            return
        
        # Store last element
        last = arr[n - 1]
        
        # Shift elements to the right
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]
        
        # Put last element at first position
        arr[0] = last

