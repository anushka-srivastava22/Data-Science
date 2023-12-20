indian = ['paneer','pakoda','samosa']
chinese = ['manchurian','fried rice', 'noodles']
italian = ['pizza','pasta','lasagnia']

dish = input("Enter a dish name : ")

if dish in indian:
    print("Indian")
elif dish in chinese:
    print("Chinese")
elif dish in italian:
    print("Italian")
else:
    print("No idea")
