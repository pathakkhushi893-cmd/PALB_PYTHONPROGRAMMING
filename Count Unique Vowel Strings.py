class Solution:
    def vowelCount(self, s):
        from math import factorial
        from collections import Counter
        
        vowels = "aeiou"
        freq = Counter(s)
        
        total_choices = 1
        distinct_vowels = 0
        
        for v in vowels:
            if freq[v] > 0:
                total_choices *= freq[v]
                distinct_vowels += 1
        
        if distinct_vowels == 0:
            return 0
        
        return total_choices * factorial(distinct_vowels)
