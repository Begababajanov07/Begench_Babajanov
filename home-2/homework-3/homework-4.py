arr = ['a', 'b', 'c', 'b', 'c', 'c']
sign = []
result =[]
for el in arr:
    if el not in sign:
        sign.append(el)
        result.append(el)
    else:
        if el in result:
            i = result.index(el)
            del result[i]
print(*result)