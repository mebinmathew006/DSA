class Trie:
    def __init__(self):
        self.root={}
        self.end_symbol='*'
        
    def insert(self,value):
        temp=self.root
        for i in value:
            if not i in temp:
                temp[i]={}
            temp=temp[i]
            
        temp[self.end_symbol]=True
        
    def search(self,patten):
        node=self.root
        for i in patten :
            if not i in node:
                return False
            
            node=node[i]
            
        return True