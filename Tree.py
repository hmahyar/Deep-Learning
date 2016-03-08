
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

class binaryHeap(object):
    def __init__(self):
        self.heapList= [0]
    
    def sync_tree(self,tree_len):
        while tree_len>0:
            print 'Check',tree_len,' ',(tree_len)//2
            if self.heapList[tree_len]<self.heapList[(tree_len)//2]:
                self.heapList[tree_len],self.heapList[(tree_len)//2]=self.heapList[(tree_len)//2],self.heapList[tree_len]
                print 'Swap'
            tree_len = (tree_len//2)

    def insert(self,node):
        self.heapList.append(node)
        print self.heapList
        self.sync_tree(len(self.heapList)-1)
        
    def print_tree(self):
        print self.heapList
T = BinaryTree(5)
for i in [3,7,1,2,6,9,8,10,4]:
    T.binery_insert(i,T.tree)
#T.traverse_tree(T.tree)

B = binaryHeap()
for i in [7,3,1,2,6,9,8,10,4]:
    B.insert(i)
    B.print_tree()
    print ('-----')




