# prefix sum or preprocessing with cumulative sums

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        
        prefix = [0] * len(words)
        
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prefix[i] = 1
        for i in range(1, len(words)):
            prefix[i] += prefix[i-1]
        
        result = []
        for li, ri in queries:
            if li > 0:
                result.append(prefix[ri] - prefix[li-1])
            else:
                result.append(prefix[ri])
        
        return result