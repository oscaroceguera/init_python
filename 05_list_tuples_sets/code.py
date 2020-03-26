l = ["Bob", "Rolf", "Anne"]  # you can add, remove elements
t = ("Bob", "Rolf", "Anne")  # you can't add, remove elements
# you can add, remove elements but you can't have duplicate element
s = {"Bob", "Rolf", "Anne"}

print(l[0])

l[0] = "OSCAR"
print(l)
# t[0] = "oscar" #error

# ADD
l.append("Chamuco")
print(l)

print(t[2])

# REMOVE
l.remove("Chamuco")
print(l)

# ADD
s.add("Oscar")
s.add("Oscar")
print(s)
