exp = [2340,2500,2100,3100,2980]
#to calculate the total 
total = 0
for i in range(len(exp)):
    print("month: ",(i+1),"expense: ",exp[i])
    
total =  total + exp[i]
print(total)