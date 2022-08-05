total = 0
def sum(a,b):
    print("a:",a)
    print("b:",b)
    
    total = a+b
    print("total inside the function:",total)
    return total


n = sum (b=5,a=6)
#name argument

# print("the total outside function: ",n )
print("the total outside function: ",total )