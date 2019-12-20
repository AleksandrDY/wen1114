"""n = 6
m = 5
data = [[0 for y in range(m)] for x in range(n)]
print(data)

for row in data:
    for element in row:
        print(element, end =' ')
    print()
print()
for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end=' ')
"""


n = 4
d2 = [[0 for y in range(n)] for x in range(n)]

for row in range (len(d2)):
    for column in range(len(d2[row])):
        d2[row][column] = (row + 1) * (column +1)
        print(d2[row][column], end=' ')
    print()
print(data)