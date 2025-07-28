class Node :
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next = None
        
class HashTable:
    def __init__(self,size=10):
        self.size=size
        self.table = [None] * size
    def __hash(self,key):
        return hash(key)%self.size
        
    def display(self):
        for i, node in enumerate(self.table):
            curr = node
            print(f"Bucket {i}:", end=" ")
            while curr:
                print(f"({curr.key}: {curr.value})", end=" -> ")
                curr = curr.next
            print("None")
        
    def insert(self, key, value):
        index = self.__hash(key)
        
        head = self.table[index]
        if not head:
            self.table[index] = Node(key, value)
            return
        current = head
        while current:
            if current.key == key:
                current.value = value
                return
            if not current.next:
                break
            current = current.next
        current.next = Node(key, value)


        
obj=HashTable()

obj.insert('kkj',333)
obj.insert('fg',434)
obj.insert('yhjh',354)
obj.insert('sdfds',756)
obj.insert('dgf',78)
obj.insert('jkjh',654)
obj.display()
            
            
            
