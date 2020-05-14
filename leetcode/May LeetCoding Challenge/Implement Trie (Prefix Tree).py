class  TrieNode:
    def __init__(self,char):
        self.char = char
        self.isWord =False
        self.children = {}




class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode("*")
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root

        for char in word:
            if char in current.children:
                current = current.children[char]
            else:

                current.children[char] = TrieNode(char)
                current = current.children[char]
        current.isWord =True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current =self.root

        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False

        if current.isWord:
            return True
        else:
            return False
        

    def startsWith(self, pre: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        prefix = True
        current = self.root
        for char in pre:
            if char in current.children:
                current = current.children[char]
            else:
                return False   
        return prefix