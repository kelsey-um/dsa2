Red = True
Black = False

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
        self.parent = None
        self.value = value
        self.colour = Black
        
class Tree:

    def __init__(self):
        self.NIL = Node(4000) #declaring NIL - 4000 will never be in the tree
        self.root = self.NIL
        
    def insert(self, value):
        
        treeInfo['nodes'] +=1
        newNode = Node(value) #creating new node
        
        #setting default nil nodes
        newNode.left = self.NIL
        newNode.right = self.NIL

        root = self.root
        nodeParent = None
        
        #looking for location
        while root != self.NIL:
            
            nodeParent = root
            
            if newNode.value < root.value:
                treeInfo['comparisons'] += 1
                root = root.left         
            else:
                treeInfo['comparisons'] += 1
                root = root.right 
        
        newNode.parent = nodeParent #location was found - insert node

        if nodeParent == None:
            self.root = newNode #tree was empty

        elif newNode.value < nodeParent.value: 
            nodeParent.left = newNode 

        else:
            nodeParent.right = newNode

        #setting new nodes children as nils
        newNode.left = self.NIL
        newNode.right = self.NIL

        newNode.colour = Red #new node starts out as red

        #fixing violations
        
        while newNode.parent and newNode.parent.colour == Red: #while parent colour is red

            if newNode.parent == newNode.parent.parent.left: #check if node's parent is a left child

                uncleNode = newNode.parent.parent.right  #uncleNode is newNode's uncle
                
                if uncleNode.colour == Red: #check if parent node and uncle node are both red
                    
                    #case 1 - parent and uncle are red
                    newNode.parent.colour = Black
                    uncleNode.colour = Black 
                    newNode.parent.parent.colour = Red #grandparent
                    newNode = newNode.parent.parent

                else:

                    if newNode == newNode.parent.right:
                        
                        #case 2 - parent is red, uncle is black, new node is a right child
                        newNode = newNode.parent 
                        self.rotateLeft(newNode)
                    
                    #case 3 - parent is red, uncle is black, new node is left child
                    newNode.parent.colour = Black
                    newNode.parent.parent.colour = Red 
                    self.rotateRight(newNode.parent.parent)
                    
            else: #same as before but with right and left swapped
                
                uncleNode = newNode.parent.parent.left 
                
                if uncleNode.colour == Red:
                    
                    newNode.parent.colour = Black
                    uncleNode.colour = Black
                    newNode.parent.parent.colour = Red
                    newNode = newNode.parent.parent

                else:

                    if newNode == newNode.parent.left:
                        
                        newNode = newNode.parent 
                        self.rotateRight(newNode)

                    newNode.parent.colour = Black
                    newNode.parent.parent.colour = Red 
                    self.rotateLeft(newNode.parent.parent)

            if newNode == self.root:
                break

        self.root.colour = Black #making sure root is always black

    def delete(self, value):

        #searching for value in tree    
        node = self.root

        #search for node
        while node != self.NIL and value != node.value:
            
            if value < node.value:
                treeInfo['comparisons'] += 1
                node = node.left

            elif value > node.value:
                treeInfo['comparisons'] += 1
                node = node.right

        if node == self.NIL: #value was not found in tree
            return
        
        treeInfo['nodes'] -= 1

        nodeX = node
        nodeXColour = nodeX.colour 
        
        # case 1 - no left child
        if node.left == self.NIL:
            nodeY = node.right 
            self.transplant(node, node.right) #replace node with its right child

        # case 2 - no right child
        elif node.right == self.NIL:
            nodeY = node.left
            self.transplant(node, node.left) #replace node with its left child

        # case 3 - node has both left and right children
        else:
            nodeX = self.minimumNode(node.right) #find minimum node in right subtree
            
            nodeXColour = nodeX.colour
            nodeY = nodeX.right 
            
            #if the minimum node's parent is the node to be delete, replace the node with its right child
            if nodeX.parent == node:
                nodeY.parent = nodeX

            else: #replace the minimum node with its right child and make the minimum node the new node to be deleted
                self.transplant(nodeX, nodeX.right)
                nodeX.right = node.right
                nodeX.right.parent = nodeX
            
            #replace the node to be deleted with the minimum node in right subtree
            self.transplant(node, nodeX)
            nodeX.left = node.left 
            nodeX.left.parent = nodeX 
            nodeX.colour = node.colour 
        
        #fixing violations
        if nodeXColour == Black:
            
            while nodeY != self.root and nodeY.colour == Black:
                
                if nodeY == nodeY.parent.left: #if nodeY is a left child
                    
                    siblingY = nodeY.parent.right #getting sibling of nodeY

                    # type 1 - sibling is red
                    if siblingY.colour == Red:
                        siblingY.colour = Black
                        nodeY.parent.colour = Red
                        self.rotateLeft(nodeY.parent)
                        siblingY = nodeY.parent.right

                    # type 2 - sibling is black and both its children are black
                    if siblingY.left.colour == Black and siblingY.right.colour == Black:
                        siblingY.colour = Red 
                        nodeY = nodeY.parent 

                    else:
                        # type 3 - sibling is black, left child is red, right child is black
                        if siblingY.right.colour == Black:
                            siblingY.left.colour = Black
                            siblingY.colour = Red
                            self.rotateRight(siblingY)
                            siblingY = nodeY.parent.right

                        # type 4 - sibling is black and its right child is red
                        siblingY.colour = nodeY.parent.colour 
                        nodeY.parent.colour = Black 
                        siblingY.right.colour = Black 
                        self.rotateLeft(nodeY.parent)
                        nodeY = self.root

                else: #if nodeY is a right child

                    siblingY = nodeY.parent.left #getting sibling of nodeY

                    # type 1 - sibling is red
                    if siblingY.colour == Red:
                        siblingY.colour = Black
                        nodeY.parent.colour = Red
                        self.rotateRight(nodeY.parent)
                        siblingY = nodeY.parent.left
                    
                    # type 2 - sibling is black and both children are black 
                    if siblingY.right.colour == Black and siblingY.left.colour == Black:
                        siblingY.colour = Red 
                        nodeY = nodeY.parent 
                    
                    else:
                        # type 3 - sibling is black, right child is red, left child is black
                        if siblingY.left.colour == Black:
                            siblingY.right.colour = Black
                            siblingY.colour = Red
                            self.rotateLeft(siblingY)
                            siblingY = nodeY.parent.left

                        # type 4 - sibling is black and its left child is red
                        siblingY.colour = nodeY.parent.colour 
                        nodeY.parent.colour = Black 
                        siblingY.left.colour = Black 
                        self.rotateRight(nodeY.parent)
                        nodeY = self.root

            nodeY.colour = Black

    def search(self, value):
    
        node = self.root

        while node != self.NIL and value != node.value:
            
            if value < node.value:
                treeInfo['comparisons'] += 1
                node = node.left

            elif value > node.value:
                treeInfo['comparisons'] += 1
                node = node.right      

        if node is not self.NIL:
            treeInfo['numbersFound'] += 1

    def getHeight(self, node=None):

        if node is None: #to handle root node
            node = self.root

        if node == self.NIL:
            return 0
        else:
            leftHeight = self.getHeight(node.left)
            rightHeight = self.getHeight(node.right)
            
        return 1 + max(leftHeight, rightHeight)
    
    def transplant(self, nodeX, nodeY): #change subtree of nodeX by subtree of nodeY

        if nodeX.parent == None: #when nodeX is the root
            self.root = nodeY
        
        elif nodeX == nodeX.parent.left: #checks if nodeX is the left child of its parent
            nodeX.parent.left = nodeY

        else: #nodeX is right child of its parent
            nodeX.parent.right = nodeY

        nodeY.parent = nodeX.parent #changes parent of nodeY

    def minimumNode(self, node): #get minimum node
        while node.left != self.NIL:
            node = node.left
        
        return node
    
    def rotateLeft(self, node):

        treeInfo['rotations'] += 1
       
        nodeX = node.right
        node.right = nodeX.left #turn nodeX's left subtree into node's right subtree 

        if nodeX.left != self.NIL: #if nodeX's left subtree is not empty then new parent is set for the subtree's root
            nodeX.left.parent = node
        
        nodeX.parent = node.parent  #switch parents

        if node.parent is None: #if node was the root, then nodeX becomes the root
            self.root = nodeX

        elif node == node.parent.left: #if node was a left child then nodeX becomes a left child
            node.parent.left = nodeX

        else: #node was a right child now nodeX becomes a right child
            node.parent.right = nodeX 

        nodeX.left = node #making node as nodeX's left child
        node.parent = nodeX #setting node's parent

    def rotateRight(self, node):
        
        treeInfo['rotations'] += 1

        nodeX = node.left 
        node.left = nodeX.right #turn nodeX's right subtree into node's left subtree

        if nodeX.right != self.NIL: #if nodeX's right subtree is not empty then new parent is set for the subtree's root
            nodeX.right.parent = node

        nodeX.parent = node.parent #switch parents

        if node.parent is None: #if node was the root, then nodeX becomes the root
            self.root = nodeX 

        elif node == node.parent.right: #if node was a right child then nodeX becomes a right child
            node.parent.right = nodeX 

        else: #node was a left child now nodeX becomes a left child
            node.parent.left = nodeX 

        nodeX.right = node #making node as nodeX's right child
        node.parent = nodeX #setting node's parent