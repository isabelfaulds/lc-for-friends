
# - need to store positions of characters

# brute force fails longer length strings
from collections import defaultdict
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        palindromes = set()

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    for k in range(i + 1, j):
                        palindromes.add(s[i] + s[k] + s[j])

        return len(palindromes)

# greedy approach
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [float('inf')] * 26
        last = [-1] * 26
        result = 0

        for i, char in enumerate(s):
            if first[ord(char) - ord('a')] == float('inf'):
                first[ord(char) - ord('a')] = i
            last[ord(char) - ord('a')] = i

        for i in range(26):
            if first[i] < last[i]:
                result +=   len(set(s[first[i] + 1:last[i]]))

        return result