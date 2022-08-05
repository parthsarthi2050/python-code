#working with json
book ={}
book["tom"] = {
    "name":"tom",
    "address":"1 red street ny",
    "phone":"1234555555"
}
book["bob"]={
        "name":"bob",
    "address":"2 red street ny",
    "phone":"1345555555"
    
}
import json
s=json.dumps(book)
with open("D://programings//python//codebasics//book.txt","w") as f:
    f.write(s)