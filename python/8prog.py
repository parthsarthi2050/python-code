indian = ["samosa","daal","naan"]
chinese = ["egg roll","pot sticker","fried rice"]
italian = ["pizza","pasta","risotto"]

dish = input("enter the name of dish ")

if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("idk this ",dish)