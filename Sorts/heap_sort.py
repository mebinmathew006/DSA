class Heap:
    def __init__(self):
        self.heap=[]
        
    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
    
    def heapify_up(self,index):
        
        if index==0:
            return
        
        parent=(index-1)//2
        
        if index < len(self.heap) and self.heap[index]> self.heap[parent]:
            self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
            
            self.heapify_up(parent)
            
    def heapify_down(self,index):
        samllest=index
        leftchild=(2*index)+1
        rightchild=(2*index)+2
        
        if leftchild<len(self.heap) and self.heap[leftchild]>self.heap[samllest]:
            samllest=leftchild
            
        if rightchild < len(self.heap) and self.heap[rightchild] > self.heap[samllest]:
            samllest=rightchild
            
        if samllest != index:
            self.heap[samllest],self.heap[index]=self.heap[index],self.heap[samllest]
            self.heapify_down(samllest)
        
            
    def remove(self):
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        
        max_value=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify_down(0)
        
        return max_value
    
    def heap_sort(self):
        sorted_list=[]
        while self.heap:
            sorted_list.append(self.remove())
            
        return sorted_list[::-1]
    
    
heap = Heap()
arr = [10, 3, 2, 8, 5, 1, 7]

for num in arr:
    heap.insert(num)
    
print("Max Heap:", heap.heap)
sorted_array = heap.heap_sort()
print("Sorted Array:", sorted_array)