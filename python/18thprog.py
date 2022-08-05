total=0
def sum(a,b=0): #default argument
    print("a:",a)
    print("b:",b)
    
    total = a+b
    print("total inside the function:",total)
    return total


n = sum (6) #but here u can still give value for b and if u dont give it will take it as zero 
#name argument

# print("the total outside function: ",n )
print("the total outside function: ",total )