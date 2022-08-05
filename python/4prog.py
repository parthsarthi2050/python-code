item1 = "bread"
item2 = "pasta"
item3 = "fruits"

#making list this way is not suitable   
items = ["bread","pasta","fruits","veggies"]
print(items)
print(items[0])
print(items[2])

#to change the string in a list
items[0] = "chips"
print(items)
#how to access range of element
print(items[0:2])
print(items[-1])

#append #to add a string in a list at last
items.append("juice")
print(items)
#to add a string in a list at a specific position
items.insert(1,"butter")
print(items)


items2 = ["shampoo","soap"]
items1 = items + items2
print(items1)

items1.insert(2,"soda")
print(items1)

print(len(items1)) #to get the length of list

# to read the list using in operator
print("bread" in items1)

