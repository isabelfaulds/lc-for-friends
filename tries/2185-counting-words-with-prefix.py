# trie - used for multiple prefix searches, large datasets
# not good use case for constraints i <= words.length <= 100 , 1 <= words[i].length, pref.length <= 100
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root # reference self.root as node
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char] # reuse the node for next depth
            node.count += 1

    def count_prefix(self, prefix):
        node = self.root
        for char in prefix:
            print(char, node.children)
            if char not in node.children:
                return 0 # break for missing
            node = node.children[char] # use next depth varaible
        return node.count
                
# one liner
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len([i for i in words if i.startswith(pref)])

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.count_prefix(pref) # trie nodes count increased n times for word in words , count reflects x / n with matching