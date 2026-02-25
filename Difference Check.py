class Solution:
    def minDifference(self, arr):
        # Convert time string to total seconds
        def to_seconds(t):
            h, m, s = map(int, t.split(':'))
            return h * 3600 + m * 60 + s
        
        # Convert all times to seconds
        times = [to_seconds(t) for t in arr]
        
        # Sort the times
        times.sort()
        
        min_diff = float('inf')
        
        # Compare adjacent times
        for i in range(1, len(times)):
            min_diff = min(min_diff, times[i] - times[i - 1])
        
        # Check circular difference (last and first across midnight)
        day_seconds = 24 * 3600
        circular_diff = day_seconds - times[-1] + times[0]
        min_diff = min(min_diff, circular_diff)
        
        return min_diff
