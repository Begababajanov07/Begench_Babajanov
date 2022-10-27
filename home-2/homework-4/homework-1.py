def func1():
  print('=====Функция 1=====')
  lst = [el**3 for el in range (20)]
  print(lst)

def func2():
  print('=====Функция 2=====')
  a = [5, 2, 'r', 4, 'ee']
  b = [4, 1, 'we', 'ee', 2, 'r']
  c = list(set(a) & set(b))
  print(c)

def runner(*args):
  if len(args) == 0:
    func1()
    func2()
  else:
    for i in args:
      globals()[i]()

runner()
runner('func1')
runner('func2')
