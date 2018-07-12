d = {}
print(d)
d["A"] = 1
d["B"] = "abcd"
d["C"] = [1,2]
print(d)

if "A" in d:
    print("A exists")

del d["A"]
print(d)

d["C"] = "1qa"
print(d)

for k in d.keys():
    print(k)
