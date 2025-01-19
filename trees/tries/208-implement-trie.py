# optimizations - 
    # no need for TrieNode() & use end of word character for search lookups
class TrieNode:
    def __init__(self):
        self.children = {}
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.inserted = set()

    def insert(self, word: str) -> None:
        self.inserted.add(word)
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

    def search(self, word: str) -> bool:
        return word in self.inserted

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)