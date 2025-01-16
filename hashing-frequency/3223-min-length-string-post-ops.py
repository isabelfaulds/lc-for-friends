from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        count = Counter(s)
        result = 0
        for string_count in count.values():
            while string_count >= 3:
                string_count -= 2 # 2 can be removed
            result += string_count
        return result

# another solution i liked
class Solution:
    def minimumLength(self, s: str) -> int:
        # odd frequency allows reducing a character count down to 1
        # even frequency allows reducing character count down to 2.
        chars = set(s)
        minLength = 0
        for c in chars:
            count = s.count(c)
            if count & 1: # odd
                minLength += 1
            elif count != 0: # even
                minLength += 2

        return minLength