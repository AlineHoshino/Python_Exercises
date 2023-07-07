from functools import reduce
a = [1, 2, 3, 4]
b = [5, 62, 7, 8]

print(list(map(lambda x, y: x+y, a, b)))


def soma(x, y):
    return x + y


lst = [1, 15, 40, 7]
print(reduce(soma, b))
print(reduce(lambda a, b: a if a > b else b, lst))

lst2 = [1, 4, 8, 10, 11, 17]
print(list(filter(lambda a: a % 2 == 0, lst2)))

print(list(zip(lst, lst2)))
