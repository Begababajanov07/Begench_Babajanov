ls = '4 0 5 0 3 0 0 5'.split(' ')
result = [i for i in ls if i != '0']
count_zero = len(ls) - len(result)
result += ['0' for _ in range(count_zero)]
print(' '.join(result))
