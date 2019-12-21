name = "Aleksandr"
print(name[2])
print(type(name[3]))

subname = name[1:5]  # 1 включительно, и до пятёрки(5), то есть двойка 2,3,4 ----->> leks
print(subname)

subname = name[4:]  # от 4 ого индекса и до конца, тк, не задано окончание
print(subname)

subname = name[:6]  # правое значение исключается. -->>
print(subname)  # ->> от начала и до 5ого индекса

print(name[::2])

# "Aleksandr"

print(name[-3])
print(name[-9])

print(name[1:7])

print(name[::-1])


