friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(local_friends)

local_abroad = abroad.difference(friends)
print(local_abroad)
