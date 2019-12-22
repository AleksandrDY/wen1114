
# Сжать строку по правилу: все последовательности повторяющихся символов длины больше 1 заменить на символ + кол-во повторений
# 'aaabbbb' -> 'a3b4'
# распечатать цепочки повторяющихся символов
value = 'aaaabbbcc' + '$'
last_change = 0
result = ''
for i in range(len(value) - 1):
    if value[i] != value[i + 1]:
        current_value = value[last_change: i + 1]
        result += value[i] + str(len(current_value))
        last_change = i + 1
print(result)

