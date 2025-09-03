class suffix_trie:
    def __init__(self,text):
        self.root={}
        self.end_symbol='*'
        self.build_suffix_trie(text)
        
    def build_suffix_trie(self,text):
        for i in range(len(text)):
            self.insert_suffix_trie(text[i:])
        
    def insert_suffix_trie(self,text):
        node=self.root
        
        for char in text:
            if char not in node:
                node[char]={}
            node=node[char]
        node[self.end_symbol]=True
        
    def search(self,pattern):
        node=self.root
        for i in range(len(pattern)):
            if not pattern[i] in node:
                return None
            node=node[pattern[i]]
        return node
    
    def autocomplete(self,pattern):
        node=self.search(pattern)
        if not node:
            return []
        return self.collect_words(node,pattern)
    
    def collect_words(self,node,pattern):
        words=[]
        if self.end_symbol in node:
            words.append(pattern)
        for char,next_node in node.items():
            if char != self.end_symbol:
                words.extend(self.collect_words(next_node,pattern+char))
        
        return words
    
trie = suffix_trie("banana")
trie.build_suffix_trie("batman")
print(trie.search(""))   # True
print(trie.search("nana"))  # True
print(trie.search("ban"))   # True
print(trie.search("xyz"))   # False
print(trie.autocomplete("b"))   # False