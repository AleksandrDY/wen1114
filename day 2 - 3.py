st = "abcabrc"
result = True
for char in st:
    #if char != "a" or char != "b" or char != "c":
    if char not in "abc":
        result = False
        print(result, st, "не состоит из abc",)
        break
print(st, "состоит из abc", result)




result = True
for char in st:
    if char not in 'abc':  # if char != 'a' or char != 'b' or char != 'c':
        result = False
        break
print(st, ' consists of abc', result)