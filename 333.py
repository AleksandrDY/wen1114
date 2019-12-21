a = 5
b = 4
c = 3

# a < b < c

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b

print(b)
