# return words containing all words2 as subsets (including multipllicity)
# hashing


# using counter
from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        w2_freq = Counter()
        for w in words2:
            w2_freq |= Counter(w)  # Element-wise max
        result = []
        for w in words1:
                result.append(w)
        return result


# without counter just for fun, default to using counter.
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        w2_freq = {}
        result = []
        for w in words2:
            w_freq = {}
            for c in w:
                w_freq[c] = w_freq.get(c,0) + 1
            for char, freq in w_freq.items():
                w2_freq[char] = max(w2_freq.get(char, 0), freq)

        for w in words1:
            w1_freq = w2_freq.copy()
            for c in w:
                if c in w1_freq:
                    w1_freq[c] -= 1
                    if w1_freq[c] == 0:
                        w1_freq.pop(c)
                    if not w1_freq:
                        result.append(w)
                        break
    # couldve also done all -  if all(w_freq.get(char, 0) >= freq for char, freq in w2_freq.items()): result.append()
        return result
