text = "ice cream"
print(text)
print(text[0])

# text[0]=a
# print(text[0]) characters in python is inmutable ....we can change the whole string but we cant change it objectively 

print(text[0:3]) #to print sub strings in python....1st index is include where as 2nd index is excluded
print(text[5:9])
print(text[:3])#if you dont specify anything it take it as zero and start it from zero
print(text[4:])

text = "hello"
print(text)

text = "let's learn "
print(text)
text = "hello 'world'"
print(text)

address = "1 purple street " #this is for single line 
address = '''1 purple street
new york
usa
america''' #this is for multi line
print(address)

s1 = "hello" 
s2 = "world"

s3 = s1 + " " + s2  # concatenating 2 strings in python
print(s3)

s4 = "total states in india are " 
num = 29

#s5 = s4 + " " + num # to add one string and one number 1st we need to change that number into string using str function
str(num)
s5 = s4 + " " + str(num) 
print(s5)
