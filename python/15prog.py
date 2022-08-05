def calculate_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total 


tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200,500,700]


tom_total= calculate_total(tom_exp_list)
joe_total= calculate_total(joe_exp_list)

print("tom's total expenses:" ,tom_total)
print("joe's total expenses:" ,joe_total)

# total = 0
# for item in tom_exp_list:
#     total= total+item
# print("tom's total expenses:",total)

# total = 0
# for item in joe_exp_list:
#     total = total + item
# print("joe's total expenses:",total)

