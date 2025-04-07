class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class BST:
    def __init__(self):
        self.root=None
    
    def append(self,data):
        node=Node(data)
        if self.root==None:
            self.root=node
            return
        temp=self.root
        while True:
            if temp.data>data:
                if temp.left:
                    temp=temp.left
                else:
                    temp.left=node
                    return
            elif temp.data < data:
                if temp.right:
                    temp=temp.right
                else:
                    temp.right=node
                    return
    def remove(self,key,node):
        if not node:
            return node
        
        if key <node.data:
            node.left=self.remove(key,node.left)        
        elif key > node.data:
            node.right=self.remove(key,node.right)
        else:
            # no child
            if not node.right and not node.left:
                return None
            
            # one child
            if not node.right:
                return node.left
                
            elif not node.left:
                return node.right
            # two child
            
            minNode=self.__min_node(node.right)
            node.data=minNode.data
            node.right=self.remove(minNode.data,node.right)
        return node
    
    def __min_node(self,node):
        while node.left:
            node=node.left
        return node
    
    def contains(self,key):
        temp=self.root
        while temp:
            if key>temp.data:
                temp=temp.right
            elif key < temp.data:
                temp=temp.left
            else:
                print(True)
                return
        print(False)
        return
    def inorder(self,node):
        # lror
        if node:
            self.inorder(node.left)
            print(node.data , end='')
            self.inorder(node.right)
    def preorder(self,node):
        if node :
            # rlr
            self.preorder(node.left)
            self.preorder(node.right)
            print(node.data ,end=',')   
obj=BST()
obj.append(50)
obj.append(55)
obj.append(57)
obj.append(52)
obj.append(51)
obj.append(49)
obj.append(48)
obj.append(47)
obj.append(45)
obj.inorder(obj.root)
print()
obj.preorder(obj.root)
obj.remove(50,obj.root)
print()
obj.contains(51)
print(obj.root.data)  
# obj.inorder(obj.root)