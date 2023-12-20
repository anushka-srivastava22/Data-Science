def calc_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total

tom_exp = [2100,3180,3300]
joe_exp = [22,4,56,76,84]

tom_total = calc_total(tom_exp)
joe_total = calc_total(joe_exp)

print("Tom's Total Expense: ",tom_total)
print("Joe's Total Expense: ",joe_total)