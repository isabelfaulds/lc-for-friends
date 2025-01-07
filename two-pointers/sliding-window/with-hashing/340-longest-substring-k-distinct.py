# maintain max sized window for unique k
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        l = 0
        chars = {}
        max_len = 0

        for r in range(len(s) ):
            chars[s[r]] = chars.get(s[r], 0) + 1
            # print(chars)
            
            while len(chars) > k:
                chars[s[l]] -= 1
                if chars[s[l]] == 0:
                    chars.pop(s[l])
                l += 1
                # print(chars)

            max_len = max( max_len , r - l + 1)
        return max_len
