sequence = [1, 3, 5, 9]
doubled = [(lambda x: x * 2)(x) for x in sequence]
print(doubled)
doubled2 = list(map(lambda x: x * 2, sequence))
print(doubled2)
