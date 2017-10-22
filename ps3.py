a = [1, -4, 6, 8, -10,11,-12, 90, 85, -3]
def func(x):
    if x > 0:
            return 1
    else:
            return 0

b = filter(func, a)
b = list(b)

b = filter(func, a)
for i in b:
    print(i)
