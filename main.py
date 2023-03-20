import random

random.seed(42) #to keep same numbers

def createSets():
    #set x

    p = random.randint(1000, 3000) # rand int between 1000 and 3000
    setX = []
    
    while len(setX) < p: # loop until length of setX is equal to p
        num = random.randint(-3000, 3000)
        
        if num not in setX: # to check for duplicates
            setX.append(num)
            
    print("Set X contains", len(setX),"integers.")

    #set y

    q = random.randint(500, 1000) # rand int between 500 and 1000
    setY = []
    
    while len(setY) < q: # loop until length of setY is equal to q
        num = random.randint(-3000, 3000)
        
        if num not in setY: # to check for duplicates
            setY.append(num)
            
    print("Set Y contains", len(setY),"integers.")

    #set z

    r = random.randint(500, 1000) # rand int between 500 and 1000
    setZ = []
    
    while len(setZ) < r: # loop until length of setZ is equal to r
        num = random.randint(-3000, 3000)
        
        if num not in setZ: # to check for duplicates
            setZ.append(num)
            
    print("Set Z contains", len(setZ),"integers.\n")

    #intersection
    xyIntersection = list(set(setX) & set(setY))
    print("Sets X and Y have",len(xyIntersection),"values in common.")

    xzIntersection = list(set(setX) & set(setZ))
    print("Sets X and Z have",len(xzIntersection),"values in common.\n")
    
    return setX, setY, setZ, xyIntersection, xzIntersection

#TODO: possibly rename class according to tree
#TODO: search tree
class Node:
    
    def __init__(self, value = None):
        self.left = None
        self.right = None
        self.value = value
        
    def insert(self, value , info):
        
        if not self.value: #to handle root bstTree
            info['nodes'] += 1
            self.value = value
            return
        
        if value < self.value: #goes to left of bstTree
            
            info['comparisons'] += 1
            
            if self.left: #there is already a bstTree on the left
                self.left.insert(value, info)
                return
            info['nodes'] += 1
            self.left = Node(value) #creating new bstTree
           
            
        if value > self.value: # goes to right of bstTree
            
            info['comparisons'] += 1
            
            if self.right: #there is already a bstTree on the left
                    self.right.insert(value, info)
                    return
            info['nodes'] += 1
            self.right = Node(value) #creating new bstTree
            
    def height(self, bstTree = None):
        
        if bstTree is None: #when at edge of tree
            return 0
    
        #checking height both children
        leftNode = self.height(bstTree.left)
        rightNode = self.height(bstTree.right)

        #max height is returned, add one to account for current bstTree
        return max(leftNode, rightNode)+1
    
    def delete(self, value, info):
        
        if self is None:
            return None

        if value < self.value:
            if self.left is not None:
                info['comparisons'] += 1
                self.left = self.left.delete(value, info)
            return self

        elif value > self.value:
            if self.right is not None:
                info['comparisons'] += 1
                self.right = self.right.delete(value, info)
            return self
        
        else:
            if self.right is None: #check if bstTree has child on right
                info['nodes'] -= 1
                return self.left
            
            if self.left is None: #check if bstTree has child on left
                info['nodes'] -= 1
                return self.right
            
            largeNode = self.right 
            while largeNode.left: # keeps iterating through all left children
                largeNode = largeNode.left

            self.value = largeNode.value #set current bstTree to smallest value in right subtree
            self.right = self.right.delete(largeNode.value, info) #deleting the bstTree that was moved
    
            return self

    def search(self,value, info):
    
        #base case
        if(self.value == value):
            # print(value,",", sep='')
            info["numbersFound"] += 1
            return self
        
        # value is greater than bstTree's value
        if self.right is not None:
            if value > self.value:
                info['comparisons'] += 1
                self.right.search(value, info)
            
        # value is less than bstTree's value
        if self.left is not None:
            if value < self.value:
                info['comparisons'] += 1
                self.left.search(value, info)
            

    def preorder(self, vals): #preorder traversal
        
        if self.value is not None: #getting value of current bstTree
            vals.append(self.value)
            
        if self.left is not None: #recursion through left bstTree
            self.left.preorder(vals)
            
        if self.right is not None: #recursion through right bstTree
            self.right.preorder(vals)
            
        return vals

setX, setY, setZ, xyIntersection, xzIntersection = createSets()

bstTreeInfo = { # holds info about tree
    'height'        : 0,
    'nodes'         : 0,
    'comparisons'   : 0,
    'numbersFound'  : 0
}

print("Inserting set X")      

bstTree = Node()

nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24]

for num in setX:
    bstTree.insert(num, bstTreeInfo)    
bstTreeInfo['height'] = bstTree.height(bstTree) #calculating tree height

print("BST: height is ", bstTreeInfo['height'], 
      ", #nodes is ", bstTreeInfo['nodes'], 
      ", #comparisons is ", bstTreeInfo['comparisons'],".\n", sep='')

print("Deleting set Y")

bstTreeInfo['comparisons'] = 0

nums = [2, 6, 20]

for num in setY:
    bstTree.delete(num, bstTreeInfo)
    
bstTreeInfo['height'] = bstTree.height(bstTree)  

    
print("BST: height is ", bstTreeInfo['height'],
      ", #nodes is ", bstTreeInfo['nodes'], 
      ", #comparisons is ", bstTreeInfo['comparisons'],"\n", sep='')

print("Searching set Z")

bstTreeInfo['comparisons'] = 0

nums = [4,2,12,18]

for num in setZ:
    bstTree.search(num, bstTreeInfo)
    
print("BST: ",
      bstTreeInfo['comparisons']," total comparisons required, ",
      bstTreeInfo['numbersFound']," numbers found, ",
      (len(setZ)-bstTreeInfo['numbersFound'])," numbers not found",
      sep='')