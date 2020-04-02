t = 5, 11
x, y = t

print(x, y)

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
print(list(student_attendance.items()))

print('---')

people = [
    ("Bob", 42, "Mechanic"),
    ("James", 24, "Artist"),
    ("Harry", 32, "Lecturer")
]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

print('---')

person = ("Bob", 42, "Mechanic")
name, _, profession = person

print(name, _, profession)

print('---')

head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)
