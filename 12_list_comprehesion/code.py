numbers = [1, 3, 5]
double = []

for num in numbers:
    double.append(num * 2)
print(double)

# Other form
other_triple = [num * 3 for num in numbers]
print(other_triple)

# --------------------

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "jen"]
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)

# Other form
my_friends = ["Oscar", "Omar", "Octavio"]
starts_0 = [friend for friend in my_friends if friend.startswith("O")]
print(starts_0)
print(my_friends is starts_0)
print("friends: ", id(my_friends), " starts_o: ", id(starts_0))
print(my_friends[0] is starts_0[0])
