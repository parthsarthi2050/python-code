f=open("D://programings//python//codebasics//speech.txt", "r")#r- read
f_out=open("D://programings//python//codebasics//speechwc.txt", "w")
# print(f.read())
# f.close()
for line in f:
    tokens=line.split(" ") #tokens are the list of words .... line.split is a seperator
    f_out.write(" wordcount:"+str(len(tokens))+line)
    # print(str(tokens))
    # print(len(tokens))
f.close()
f_out.close()