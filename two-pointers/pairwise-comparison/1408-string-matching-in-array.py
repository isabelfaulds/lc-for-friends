# Constraints of words are small - brute force o n 2 solution with hashing could technically still pass 
# could sort by string length shortest first and use pairwise comparison to compare shorter with larger
# trie prefix tree for string storage & substring search, traverse the trie to check if a string is a substring
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key = len)
        l = 0 
        r = 1
        print(words)
        result = []
        while l < len(words) - 1:
            if words[l] not in words[r]:
                if r < len(words) - 1:
                    r += 1
                else:
                    l += 1
                    r = l + 1
            else:
                result.append(words[l])
                l += 1
                r = l + 1
            
        print(words, result)
        return result
        