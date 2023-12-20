d = {"tom":7238924743,"rob":9834726845, "joe":9320342765}
print(d,"\n")
print(d["tom"],"\n")

d["sam"]=9345678291
print(d,"\n")

del d["rob"]
print(d,"\n")

for key in d:
    print("key:",key,"value:",d[key])