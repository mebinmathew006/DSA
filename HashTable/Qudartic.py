class HashTable:
    def __init__(self,size=10):
        self.size = size
        self.table = [None]*self.size
        
    def __hash(self,key):
        return hash(key)%self.size
        
    def insert(self,key,value):
        index = self.__hash(key)
        i=0
        while self.table[index]!=None and self.table[index][0]!=key:
            index = (self.__hash(key)+i*i)%self.size
            if index == i:
                raise Exception('Table is full')
            i+=1
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
