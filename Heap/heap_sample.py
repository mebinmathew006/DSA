class Heaps:
    def __init__(self):
        self.heap=[]
    
    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
        
    def parent(self,index):
        return (index-1)//2
    
    def left_child(self, index):
        return (2*index)+1
    
    def right_child(self, index):
        return (2*index)+2
        
    def heapify_up(self,index):
        parent=self.parent(index)
        
        if index>0 and self.heap[index] < self.heap[parent]:
            
            self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
            self.heapify_up(parent)
            
    def display(self):
        print(self.heap)
        
    def remove(self):
        if not self.heap:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        
        min_value=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify_down(0)
        
        return min_value
        
    def heapify_down(self,index):
        smallest=index
        left_child=self.left_child(index)
        right_child=self.right_child(index)
        
        if left_child<len(self.heap) and self.heap[left_child]<self.heap[smallest]:
            smallest=left_child
        if right_child<len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest=right_child
            
        if smallest != index:
            self.heap[smallest],self.heap[index]=self.heap[index],self.heap[smallest]
            self.heapify_down(smallest)
        
            
            
min_heap = Heaps()
min_heap.insert(10)
# min_heap.insert(5)
# min_heap.insert(15)
# min_heap.insert(2)
# min_heap.insert(1)
min_heap.display()
min_heap.remove()
min_heap.display()
