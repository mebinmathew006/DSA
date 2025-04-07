class Trie:
    def __init__(self):
        self.root={}
        self.end='*'
        
    def insert_suffix(self,text):
        for i in range(len(text)):
            self.insert_prefix(text[i:])
    
    def insert_prefix(self,text):
        node=self.root
        for i in text:
            if not i in node:
                node[i]={}
            node=node[i]
        node[self.end]=True
        
    def search(self,text):
        node=self.root
        for i in text:
            if not i in node:
                return None
            node=node[i]
        return node
        
    def autocomplete(self,text):
        node=self.search(text)
        if not node:
            return []
        return self.collect_words(node,text)
        
    def collect_words(self,node,text):
        words=[]
        for char,child in node.items():
            if char=='*':
                words.append(text)
            else:
                words.extend(self.collect_words(child,text+char))
        
        return words
    
# Example Usage:
trie = Trie()
words = ["banana", "band", "bat", "ball"]
for word in words:
    trie.insert_prefix(word)
trie.insert_suffix('bahubali')
print(trie.root)
print("Autocomplete for 'ba':", trie.autocomplete("a"))
# Output might be: ['banana', 'band', 'bat', 'ball']
        