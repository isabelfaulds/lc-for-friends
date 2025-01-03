# Greedy approach - algorithm makes the choice that seems the best at the moment
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # terminate early by looking at longest -> shortest
        dictionary.sort(key=lambda x: (-len(x), x))
        print(dictionary )
        

        def can_form_word(word):
            i , j = 0 , 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            return j == len(word)

        for word in dictionary:
            if can_form_word(word):
                return word
        return ""

# simplifying can_form_word with iterator
# O(N∗M∗Log(M))
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        def can_form_word(word):
            # needs to be iterated on 
            it = iter(s)
            return all(char in it for char in word)

        
        for word in dictionary:
            if can_form_word(word):
                return word

        return ""

# only sorting if it's a match
# O(N∗M∗Log(M))
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        def can_form_word(word):
            # needs to be iterated on 
            it = iter(s)
            return all(char in it for char in word)

        longest_word = ""
        
        for word in dictionary:
            if can_form_word(word) and ( ( len(word) > len(longest_word) ) or (len(word) == len(longest_word) and word < longest_word) ):
                longest_word = word

        return longest_word
