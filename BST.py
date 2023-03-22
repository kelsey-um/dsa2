treeInfo = { # holds info about tree
    'height'        : 0,
    'nodes'         : 0,
    'comparisons'   : 0,
    'numbersFound'  : 0
}

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.height = 1

class Tree:
        
    def insert(self, node, value):

        #when node is not set
        if not node:
            treeInfo['nodes'] += 1
            return Node(value)
        
        elif value < node.value: #value is less than that of current node, i.e. go to left
            
            treeInfo['comparisons'] += 1
            node.left = self.insert(node.left, value)
        
        elif value > node.value: #value is more than that of current node, i.e. go to right
            
            treeInfo['comparisons'] +=1 
            node.right = self.insert(node.right, value)

        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))

        return node

    def delete(self, node, value): 

        if not node: #if node is not set
            return node

        elif value < node.value: #value is less than that of node, i.e. go to left
            
            treeInfo['comparisons'] +=1 
            node.left = self.delete(node.left, value)

        elif value > node.value: #value is more than that of node, i.e. go to right
            
            treeInfo['comparisons'] +=1 
            node.right = self.delete(node.right, value)
        
        else:
            if node.left is None: #check if node has child on left
                treeInfo['nodes'] -= 1
                nodeX = node.right
                node = None

                return nodeX
            
            elif node.right is None: #check if node has child on left
                treeInfo['nodes'] -= 1
                nodeX = node.left
                node = None

                return nodeX
            
            #both children are not none therefore find node with min value in the right subtree
            nodeX = self.minimumNode(node.right) #get the minimum value from right
            node.value = nodeX.value #value of current node is replaced
            node.right = self.delete(node.right ,nodeX.value) #delete node that was moved up

        if node is None:
            return node
        
        #updating height
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
    
        return node

    def search(self, node, value):
    
        #when node is found
        if(node.value == value):
            treeInfo["numbersFound"] += 1
            return node
        
        # value is greater than node's value
        if node.right is not None:
            if value > node.value:
                treeInfo['comparisons'] += 1
                self.search(node.right,value)
            
        # value is less than node's value
        if node.left is not None:
            if value < node.value:
                treeInfo['comparisons'] += 1
                self.search(node.left,value)
   

    def minimumNode(self, root):
        if root is None or root.left is None:
            return root
        return self.minimumNode(root.left)
    
    def getHeight(self, node):

        if not node: #if node is not set
            return 0
        
        return node.height


