import math


def convert_hash_to_array(hash):
    if hash == {}:
        return []
    arr = list()
    hash2 = dict(sorted(hash.items()))
    for item in hash2:
        arr.append([item, hash[item]])

    return arr


print(
    convert_hash_to_array(
        {"name": "Jeremy", "age": 24, "role": "Software Engineer"}
    )
)


def is_square(n):
    x = math.pow(n, 1/2)
    string_x = str(x)
    arr_str = string_x.split('.')
    if arr_str[1] == '0':
        return True
    return False


print(is_square(0))


# def is_square1(n):

#     if n < 0:
#         return False

#     sqrt = math.sqrt(n)
#     return sqrt.is_integer()
# solution in codewars
