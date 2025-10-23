def func(a, b, c):
    print(a, b, c)

kwargs = {'a': 1, 'c': 2, 'b': 3}
func(**kwargs)      # 1 2 3  ← распаковка словаря по ключам