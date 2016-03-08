
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

    

T = BinaryTree(5)
T.binery_insert(3,T.tree)
T.binery_insert(7,T.tree)
T.binery_insert(1,T.tree)
T.binery_insert(2,T.tree)
T.binery_insert(6,T.tree)
T.binery_insert(9,T.tree)
T.binery_insert(8,T.tree)
T.binery_insert(10,T.tree)
T.binery_insert(4,T.tree)
T.traverse_tree(T.tree)


