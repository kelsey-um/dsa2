treeInfo = { # holds info about tree
    'height'        : 0,
    'nodes'         : 0,
    'comparisons'   : 0,
    'numbersFound'  : 0,
    'rotations'     : 0
}

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.height = 1

class Tree:
    
    def insert(self, node, value):

        if not node: #when node is not set
            treeInfo['nodes'] += 1
            return Node(value)
        
        elif value < node.value: #value is less than that of current node, i.e. go to left

            treeInfo['comparisons'] += 1
            node.left = self.insert(node.left, value)

        elif value > node.value: #value is more than that of current node, i.e. go to right
            
            treeInfo['comparisons'] += 1 
            node.right = self.insert(node.right, value)

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        #calculate balance factor
        balance = self.getBalance(node)

        if balance > 1: #height of left subtree is greater than of right subtree
            if value < node.left.value: #if value is less than the lefts value
                return self.rotateRight(node)
            
            else:
                node.left = self.rotateLeft(node.left)
                return self.rotateRight(node)

        if balance < -1: #height of right subtree is greater than of left subtree
            if value > node.right.value: #if value is less than the rights value 
                return self.rotateLeft(node)
            
            else:
                node.right = self.rotateRight(node.right)
                return self.rotateLeft(node)

        return node
    
    def delete(self, node, value):

        if not node:
            return node
        
        elif value < node.value: #value is less than that of node, i.e. go to left

            treeInfo['comparisons'] += 1
            node.left = self.delete(node.left, value)

        elif value > node.value: #value is more than that of node, i.e. go to right

            treeInfo['comparisons'] += 1
            node.right = self.delete(node.right, value)

        else: #when node to be deleted has two children

            if node.left is None: #current node is replaced with its right child
                treeInfo['nodes'] -= 1
                nodeX = node.right
                node = None

                return nodeX
            
            elif node.right is None: #current node is replaced with its left child
                treeInfo['nodes'] -= 1
                nodeX = node.left
                node = None

                return nodeX
            
            #both children are not none therefore find node with min value in the right subtree
            nodeX = self.minimumNode(node.right) #get the minimum value from right
            node.value = nodeX.value #value of current node is replaced
            node.right = self.delete(node.right, nodeX.value) #delete node that was moved up 
        
        if node is None:
            return node

        #calculate balance factor
        balance = self.getBalance(node)

        if balance > 1: #height of left subtree is greater than of right subtree
            if self.getBalance(node.left) >= 0: #checking is left subtree is balanced
                return self.rotateRight(node)
            
            else:
                node.left = self.rotateLeft(node.left)
                return self.rotateRight(node)

        if balance < -1: #height of right subtree is greater than of left subtree
            if self.getBalance(node.right) <= 0: #checking if right subtree is balanced
                return self.rotateLeft(node)
            
            else:
                node.right = self.rotateRight(node.right)
                return self.rotateLeft(node)
        
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

    def getHeight(self, node): #to calculate height
        
        if not node: #if node is not set
            return 0
        
        return node.height
    
    def getBalance(self, node):

        if not node:
            return 0
        
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def rotateLeft(self, node):
        
        treeInfo['rotations'] += 1
        
        nodeX = node.right #setting nodeX as the node's right child
        nodeY = nodeX.left #setting nodeY as nodeX's left child
       
        #promoting nodeX to root of subtree and demoting node to left child of nodeX
        nodeX.left = node #node is set as nodeX's left child
        node.right = nodeY #right child of node is set to nodeY

        #recalculating heights accordingly
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        nodeX.height = 1 + max(self.getHeight(nodeX.left), self.getHeight(nodeX.right))

        return nodeX #the new root of subtree
    
    def rotateRight(self, node):
        
        treeInfo['rotations'] += 1
        
        nodeX = node.left #setting nodeX as the node's left child
        nodeY = nodeX.right #setting nodeY as nodeX's right child

        #promoting nodeX to root of subtree and demoting node to right child of nodeX
        nodeX.right = node #node is set as nodeX's right child
        node.left = nodeY #right child of node is set to nodeY

        #recalculating heights accordingly
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        nodeX.height = 1 + max(self.getHeight(nodeX.left), self.getHeight(nodeX.right))

        return nodeX #the new root of subtree

    def minimumNode(self, root): #get minimum node
        if root is None or root.left is None:
            return root
        
        return self.minimumNode(root.left)