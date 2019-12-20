a =10
b =20
values = [x ** 2 for x in range(a, b + 1)]

#values = []
#for x in range(a, b +1):
#    values.append(x ** 2)
print(values)

values =[x for x in values if x % 2 == 0]
print(values)

values = [100 if x < 200 else 400 for x in values]
print(values)


