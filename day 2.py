"""Подсчитать количество вхождений определенного символа
 в строку, напечатать процентное
  содержание символа в строке.

    'aaabbb' 'a' -> 3 50.0%
"""

st = "aabbbbb"
symbol = "b"

count = 0
for char in st:
    if char == symbol:
        count += 1

print(count,"элементов в строке", (count/len(st)) * 100,"% заполнения строки")
