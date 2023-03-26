from Sets import *
import BST
import AVL
import RBT

#creating sets
setX, setY, setZ, xyIntersection, xzIntersection = createSets() 

#declaring all trees and nodes
bstTree = BST.Tree()
bstNode = None

avlTree = AVL.Tree()
avlNode = None

rbtTree = RBT.Tree()

#inserting set x into tress
print("Inserting set X")    

for num in setX:
    bstNode = bstTree.insert(bstNode, num)  
    avlNode = avlTree.insert(avlNode, num)
    rbtTree.insert(num)

#setting heights
BST.treeInfo['height'] = bstNode.height
AVL.treeInfo['height'] = avlNode.height 
RBT.treeInfo['height'] = rbtTree.getHeight()


#printing results
print("BST: height is ", BST.treeInfo['height'], 
    ", #nodes is ", BST.treeInfo['nodes'], 
    ", #comparisons is ", BST.treeInfo['comparisons'],".", sep='')

print("AVL: ", AVL.treeInfo['rotations']," rotations req."
    ", height is ", AVL.treeInfo['height'], 
    ", #nodes is ", AVL.treeInfo['nodes'], 
    ", #comparisons is ", AVL.treeInfo['comparisons'],".", sep='')

print("RBT: ", RBT.treeInfo['rotations']," rotations req."
    ", height is ", RBT.treeInfo['height'], 
    ", #nodes is ", RBT.treeInfo['nodes'], 
    ", #comparisons is ", RBT.treeInfo['comparisons'],".\n", sep='')


#deleting set y from trees
print("Deleting set Y")

#setting comparsions and rotations back to 0
BST.treeInfo['comparisons'] = 0 
AVL.treeInfo['comparisons'] = 0
AVL.treeInfo['rotations'] = 0
RBT.treeInfo['comparisons'] = 0
RBT.treeInfo['rotations'] = 0

for num in setY:
    bstNode = bstTree.delete(bstNode, num)
    avlNode = avlTree.delete(avlNode, num) 
    rbtTree.delete(num)

BST.treeInfo['height'] = bstNode.height #setting height
AVL.treeInfo['height'] = avlNode.height
RBT.treeInfo['height'] = rbtTree.getHeight()
    
#printing results
print("BST: height is ", BST.treeInfo['height'],
    ", #nodes is ", BST.treeInfo['nodes'], 
    ", #comparisons is ", BST.treeInfo['comparisons'],"", sep='')

print("AVL: ", AVL.treeInfo['rotations']," rotations req."
      ", height is ", AVL.treeInfo['height'],
      ", #nodes is ", AVL.treeInfo['nodes'], 
      ", #comparisons is ", AVL.treeInfo['comparisons'], sep='')

print("RBT: ", RBT.treeInfo['rotations']," rotations req."
      ", height is ", RBT.treeInfo['height'],
      ", #nodes is ", RBT.treeInfo['nodes'], 
      ", #comparisons is ", RBT.treeInfo['comparisons'],"\n", sep='')
    

print("Searching set Z")

#setting comparisons back to 0
BST.treeInfo['comparisons'] = 0 
AVL.treeInfo['comparisons'] = 0
RBT.treeInfo['comparisons'] = 0

for num in setZ:
    bstTree.search(bstNode, num)
    avlTree.search(avlNode, num)
    rbtTree.search(num)
   
#printing results
print("BST: ",
    BST.treeInfo['comparisons']," total comparisons required, ",
    BST.treeInfo['numbersFound']," numbers found, ",
    (len(setZ)-BST.treeInfo['numbersFound'])," numbers not found",
    sep='')

print("AVL: ",
    AVL.treeInfo['comparisons']," total comparisons required, ",
    AVL.treeInfo['numbersFound']," numbers found, ",
    (len(setZ)-AVL.treeInfo['numbersFound'])," numbers not found",
    sep='')

print("RBT: ",
    RBT.treeInfo['comparisons']," total comparisons required, ",
    RBT.treeInfo['numbersFound']," numbers found, ",
    (len(setZ)-RBT.treeInfo['numbersFound'])," numbers not found\n",
    sep='')