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
        self.NIL = Node(4000) #declaring NIL 
        self.root = self.NIL
        
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

    def insert(self, value):
        
        treeInfo['nodes'] +=1
        newNode = Node(value) #creating new node
        
        #setting default nil nodes
        newNode.left = self.NIL
        newNode.right = self.NIL

        root = self.root
        nodeParent = self.NIL
        
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

        if nodeParent == self.NIL:
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
        
        # while newNode.parent.colour == Red: #while parent colour is red
        while newNode.parent and newNode.parent.colour == Red: #while parent colour is red

            if newNode.parent == newNode.parent.parent.left: #check if node's parent is a left child

                uncleNode = newNode.parent.parent.right  #uncleNode is newNode's uncle
                
                if uncleNode.colour == Red: #check if parent node and uncle node are both red
                    
                    #case 1 - modify accordingly
                    newNode.parent.colour = Black
                    uncleNode.colour = Black 
                    newNode.parent.parent.colour = Red
                    newNode = newNode.parent.parent

                else:

                    if newNode == newNode.parent.right:
                        
                        #case 2 - modify accordingly
                        newNode = newNode.parent 
                        self.rotateLeft(newNode)
                    
                    #case 3 - modify accordingly
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

    def getHeight(self, node=None):

        if node is None: #to handle root node
            node = self.root

        if node == self.NIL:
            return 0
        else:
            leftHeight = self.getHeight(node.left)
            rightHeight = self.getHeight(node.right)
            
        return 1 + max(leftHeight, rightHeight)
