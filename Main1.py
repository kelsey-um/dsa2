from Sets import *
import BST
import AVL
import RBT

setX, setY, setZ, xyIntersection, xzIntersection = createSets()

bstTree = BST.Tree()
bstNode = None

print("Inserting set X")    

for num in setX:
    bstNode = bstTree.insert(bstNode, num)  
    
BST.treeInfo['height'] = bstNode.height

print("BST: height is ", BST.treeInfo['height'], 
    ", #nodes is ", BST.treeInfo['nodes'], 
    ", #comparisons is ", BST.treeInfo['comparisons'],".\n", sep='')

print("Deleting set Y")

BST.treeInfo['comparisons'] = 0

# nums = [2, 6, 20]

for num in setY:
    bstNode = bstTree.delete(bstNode, num)
    
BST.treeInfo['height'] = bstNode.height
    
print("BST: height is ", BST.treeInfo['height'],
    ", #nodes is ", BST.treeInfo['nodes'], 
    ", #comparisons is ", BST.treeInfo['comparisons'],"\n", sep='')

print("Searching set Z")

BST.treeInfo['comparisons'] = 0

for num in setZ:
    bstTree.search(bstNode,num)
    
print("BST: ",
    BST.treeInfo['comparisons']," total comparisons required, ",
    BST.treeInfo['numbersFound']," numbers found, ",
    (len(setZ)-BST.treeInfo['numbersFound'])," numbers not found\n\n\n\n",
    sep='')






avlTree = AVL.Tree()
avlNode = None

print("Inserting set X")    

for num in setX:
    avlNode = avlTree.insert(avlNode, num)  
    
AVL.treeInfo['height'] = avlNode.height

print("AVL: ", AVL.treeInfo['rotations']," rotations req."
    ", height is ", AVL.treeInfo['height'], 
    ", #nodes is ", AVL.treeInfo['nodes'], 
    ", #comparisons is ", AVL.treeInfo['comparisons'],".\n", sep='')

print("Deleting set Y")

AVL.treeInfo['comparisons'] = 0
AVL.treeInfo['rotations'] = 0

for num in setY:
    avlNode = avlTree.delete(avlNode, num)
    
AVL.treeInfo['height'] = avlNode.height
    
print("AVL: ", AVL.treeInfo['rotations']," rotations req."
      ", height is ", AVL.treeInfo['height'],
      ", #nodes is ", AVL.treeInfo['nodes'], 
      ", #comparisons is ", AVL.treeInfo['comparisons'],"\n", sep='')

print("Searching set Z")

AVL.treeInfo['comparisons'] = 0

for num in setZ:
    avlTree.search(avlNode, num)
    
print("AVL: ",
    AVL.treeInfo['comparisons']," total comparisons required, ",
    AVL.treeInfo['numbersFound']," numbers found, ",
    (len(setZ)-AVL.treeInfo['numbersFound'])," numbers not found\n\n\n\n",
    sep='')