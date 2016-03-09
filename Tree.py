
class BinaryTree(object):
    def __init__(self,rootnode):
        self.tree=[rootnode,[],[]]

    def sort(self,tree):
        if tree:
            if tree[1]:
                self.sort(tree[1])
            print (tree[0])
            if tree[2]:
                self.sort(tree[2])
            
    
    def binery_insert(self,node,tree):
        if len(tree)==0:
            tree.append(node)
            tree.append([])
            tree.append([])

        if tree[0]==node:
            return 'Already Exists'
        elif tree[0]>node: 
            self.binery_insert(node,tree[1])
        else:
            self.binery_insert(node,tree[2])

    def max(self,tree):
        if tree[2]:
            return self.max(tree[2])
        else:
            return tree[0] 
    
    def min(self,tree):
        if tree[1]:
            return self.min(tree[1])
        else:
            return tree[0] 

T = BinaryTree(5)
for i in [3,7,1,2,16,20,6,9,8,10,12,15,11,19,3]:
    T.binery_insert(i,T.tree)
#print T.sort(T.tree)
print 'Max: ',T.max(T.tree)
print 'Min: ',T.min(T.tree)



