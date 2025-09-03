class HashTable:
    def __init__(self,size=10):
        self.size = size
        self.table = [None]*self.size
        
    def __hash(self,key):
        return hash(key)%self.size
        
    def __hash2(self,key):
        return 1+(hash(key)%(self.size-1))
        
    def insert(self,key,value):
        index = self.__hash(key)
        step = self.__hash2(key)
        i=0
        while self.table[index]!=None and self.table[index][0]!=key:
            i+=1
            index = (self.__hash(key)+i*step)%self.size
            
            if index == self.size:
                raise Exception('Table is full')
            
        self.table[index]=(key,value)
        
    def display(self):
        for i in self.table:
            if i != None:
                print(f'{i[0]}:{i[1]}')
            
h1 =HashTable()
h1.insert('dfd',33)
h1.insert('dgf',33)
h1.insert('hgh',33)
h1.insert('jfgh',33)
h1.insert('ert',33)
h1.insert('ert',4656)
h1.display()
