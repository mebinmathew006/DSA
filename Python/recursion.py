class MyRange:
    def __init__(self,start,end):
        self.current = start
        self.end = end
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.current>self.end:
            raise StopIteration
        self.current =+1
        return self.current 
        
r =MyRange(1,10)

for i in r:
    print(i)
