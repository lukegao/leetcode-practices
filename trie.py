
class Node:
    def __init__(self, c=''):
        self.c = c
        self.children = {}
        self.end = False
    
    def insert(self, word):
        cur = self
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = Node(letter)
            cur = cur.children[letter]
    
    def search(self, word):
        cur = self
        for i, letter in enumerate(word):
            if letter is '.':
                for child in cur.children.values():
                    if child.search(word[i+1:]):
                        return True
                return False
            elif letter in cur.children:
                cur = cur.children[letter]
            else:
                return False
        return True


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.root.insert(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.root.search(word)


if __name__ == '__main__':
    w = WordDictionary()

    w.addWord('a')
    w.addWord('a')
    print(w.search('.'))
    print(w.search('a'))
    print(w.search('aa'))
    print(w.search('a'))
    print(w.search('a.'))
    print(w.search('.a'))