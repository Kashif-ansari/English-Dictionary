import json
from numpy import array
data=json.load(open('data.json'))

mid = len(data)
print(mid)



"""
count = 0
for i in data.keys():
    key[count] = i
    
    count+=1
count = 0
for i in data.values():
        value[count] = str(i[0])
        
        count+=1
print(key)"""

k = open("keys.txt","r")
key = array([0 for i in range(2610)], dtype = 'object')
for i in range(len(key)):
    key[i] = k.readline()
value = array([0 for i in range(2610)], dtype = 'object')
v = open("values.txt","r")
for i in range(len(value)):
    value[i] = v.readline()


print(key[len(key)-1])
print(value[len(key)-1])

midpoint = len(key)//2
print(key[midpoint])

"""
print(key)
print(value)

with open("keys.txt","a") as k:
    for i in range(len(key)):
        k.write(key[i]+"\n")
        
with open("values.txt","a") as v:
    for i in range(len(value)):
        v.write(value[i]+"\n")

for i in range(len(key)):
    print(key[i])
    
print(value)
for i in range(len(value)):
    print(value[i])"""