
import bisect
import copy

my_array = [1, 2, 3, 'teste', False, True, 0.1]
print(my_array[0])
print(my_array[-1])
print(my_array[1:3])
print(my_array[len(my_array) - 1])
my_array = [7, 6, 5, 4, 3]
my_array.sort()
print(my_array)
my_array_2 = [23, 5, 4]
array_sorted = (sorted(my_array_2))
print(my_array_2)
print(array_sorted)

my_array.insert(0, 999)  # insira na posição 0 o numero 999
print(my_array)  # fica lento se tiver muitos dados porque move todos os itens
my_array.append(456)  # mais rápido
print(my_array)
my_array.remove(999)  # lento também, porque movimenta os itens
print(my_array)
# quero remover o item 4, pode setar como None
my_array[1] = None
print(my_array)
# 2 solução
del my_array[1]
print(my_array)
print(min(my_array))
print(max(my_array))

# deixe o array ordenado e depois faça uma busca
print(bisect.bisect(my_array, 5))  # O(log n)
# inserindo item
bisect.insort(my_array, 888)
print(bisect.bisect(my_array, 888))
my_array_3 = range(4)  # cria o range
print(list(my_array_3))  # cria a lista [0, 1, 2, 3]
two_dimensions_array = [[123, 456], [789, 321]]
A = [1, 2, 3]
B = A
B[0] = 999
print(A)  # desse jeito se eu altero B também altero o A

a = [1, 2, 3]
b = a
b = list(a)  # cópia do valor do a
b[0] = 999
print(a)
print(b)

a = [{'teste': 999, 'bbb': 466}]
b = a
b[0]['teste'] = 555
print(a)
print(b)
# troca a e b

# se quero uma cópia
b = copy.copy(a)

b[0]['teste'] = 333
print(a)

a = [{'teste': 999, 'bbb': 466}]
b = copy.deepcopy(a)  # muito bom para cópia de dicionários
b[0]['teste'] = 1
print(a)
print(b)

a = [1, 2, 3, 4]

a[2], a[1] = a[1], a[2]  # quero trocar os elemtnos de posição
print(a)


def solution(numbers, target_sum):
    for i in range(len(numbers) - 1):
        if numbers[i] + numbers[i+1] == target_sum:
            return [numbers[i], numbers[i+1]]
    return []


print(solution([1, 4], 5))


def add(a, b):
    return a + b


def pow(a, b):
    return a**b


def zip_with(fn, a1, a2):
    new_arr = list()
    if len(a1) == len(a2):
        for num in range(len(a1)):
            result = fn(a1[num], a2[num])
            new_arr.append(result)
    if len(a1) < len(a2):
        for num in range(len(a1)):
            result = fn(a1[num], a2[num])
            new_arr.append(result)
    if len(a2) < len(a1):
        for num in range(len(a2)):
            result = fn(a1[num], a2[num])
            new_arr.append(result)
    return new_arr


def zip_with2(fn, a1, a2):
    return list(map(fn, a1, a2))


print(zip_with2(pow, [10, 10, 10, 10, 15], [0, 1, 2, 3]))


# Understanding map() loops over the items of an input iterable (or iterables)
# and returns an iterator that results from applying a transformation function
#  to every item in the original input iterable.
# According to the documentation, map() takes a function object and an iterable
# (or multiple iterables) as arguments and returns an iterator that yields
# transformed items on demand. The function’s signature is defined as follows:
# map(function, iterable[, iterable1, iterable2,..., iterableN])
# first_it = [1, 2, 3]
# second_it = [4, 5, 6, 7]
# list(map(pow, first_it, second_it))
# [1, 32, 729]
# pow() takes two arguments, x and y, and returns x to the power of y. In the
# first iteration, x will be 1, y will be 4, and the result will be 1.
# In the second iteration,
#  x will be 2, y will be 5, and the result will be 32, and so on. The final
# iterable is only as long as the shortest iterable,
#  which is first_it in this case.

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

print(tuple(x))
