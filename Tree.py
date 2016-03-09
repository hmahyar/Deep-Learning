
class BinaryTree(object):
    def __init__(self,rootnode):
        self.tree=[rootnode,[],[]]

    def traverse_tree(self,tree):
        if tree:
            
            if tree[1]:
                self.traverse_tree(tree[1])
            print (tree[0])
            if tree[2]:
                self.traverse_tree(tree[2])
            
    
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
for i in [3,7,1,2,6,9,8,10,4]:
    T.binery_insert(i,T.tree)
#T.traverse_tree(T.tree)
print 'max: ',T.max(T.tree)
print 'min: ',T.min(T.tree)



