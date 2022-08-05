d={"tom":1234567891,"rob":2345678901,"joe":333333333333}
print(d)
print(d["tom"])
# add new 
d["sam"]=435654365437
print(d)
# delete 
del d["tom"]
print(d)
# print all the value
for key in d:
    print("key:",key,"value:",d[key])
    
for k,v in d.items():
    print("key:",key,"value:",v)
    
    
    
    
print("tom" in d)

d.clear()
print(d)
""" list all the values have similar meaning(homoh=geneous)
tuple : all the values have different meaning(heterogeneous)"""

point = (5,9)
print(point[0])
#tuple are inmutable
