name = "Oscar"
greeting = "Hello {}"
with_name = greeting.format(name)
with_name_two = greeting.format('Eduardo')
longer_phrasee = "Hola {}, Hoy es {}"
formatted = longer_phrasee.format("Carlos", "martes")

print(with_name)
print(with_name_two)
print(formatted)
