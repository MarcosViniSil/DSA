#Link to problem: https://leetcode.com/problems/implement-trie-prefix-tree/
#Time complexity: O(n)
#Space complexity: O(n)
                        
class Node:
    def __init__(self):
        self.childreen = [None] * 26
        self.isEnd = False

class Trie:
    def __init__(self):
        self.head = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        aux = self.head
        for i,letter in enumerate(word):
            idx = ord('a') - ord(letter)
            if aux[idx] is None:
                aux[idx] = Node()
            
            if i == len(word) - 1:
                aux[idx].isEnd = True

            aux = aux[idx].childreen
        
    def search(self, word: str) -> bool:
        aux = self.head
        
        for i,letter in enumerate(word):
            idx = ord('a') - ord(letter)
            if aux[idx] is None:
                return False
            
            if i == len(word) - 1:
                return aux[idx].isEnd

            aux = aux[idx].childreen
        
    def startsWith(self, prefix: str) -> bool:
        aux = self.head
        
        for i,letter in enumerate(prefix):
            idx = ord('a') - ord(letter)
            if aux[idx] is None:
                return False
        
            aux = aux[idx].childreen
        return True
