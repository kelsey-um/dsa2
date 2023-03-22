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