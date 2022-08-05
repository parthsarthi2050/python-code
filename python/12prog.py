key_loaction = "chair"
locations = ["garage","living room","chair","closet"]
for i in locations:
    if i==key_loaction:
        print("key found in ",i)
        break
    else:
        print("key not found in ",i)