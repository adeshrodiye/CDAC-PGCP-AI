from CarClass import Car

c1 = Car("Tata","Safari",500000)
c2 = Car("Honda","city",1000000)

print(c1)
print(c1.calculate_premium(2))
print(c1.calculate_premium(3))

Car.show_count()

c1._price = 20000

data = "kia,seltos,1500000"
c3 = Car.from_string(data)
print(c3)
print(type(c3))

c4 = eval(repr(c2))
print(c4)
print(type(c4))

