import random


#set x

p = random.randint(1000, 3000)
setX = []
  
while len(setX) < p:
    num = random.randint(-3000, 3000)
    
    if num not in setX:
        setX.append(num)
        
print("Set X contains", len(setX),"integers.")

#set y

q = random.randint(500, 1000)
setY = []
  
while len(setY) < q:
    num = random.randint(-3000, 3000)
    
    if num not in setY:
        setY.append(num)
        
print("Set Y contains", len(setY),"integers.")

#set z

r = random.randint(500, 1000)
setZ = []
  
while len(setZ) < r:
    num = random.randint(-3000, 3000)
    
    if num not in setY:
        setZ.append(num)
        
print("Set Z contains", len(setZ),"integers.\n")

#intersection
xyIntersection = list(set(setX) & set(setY))
print("Sets X and Y have",len(xyIntersection),"values in common.")

xzIntersection = list(set(setX) & set(setZ))
print("Sets X and Z have",len(xzIntersection),"values in common.\n")
