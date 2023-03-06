# def find_uniq(arr):
#     count_number = dict()
#     for item in arr:
#         if item in count_number:
#             count_number[item] += 1
#         else:
#             count_number[item] = 1
#     for item in count_number:
#         if count_number[item] == 1:
#             return item
#     return


# print(find_uniq([1, 1, 1, 2, 1]))


# def find_uniq2(arr):
#     a, b = set([1, 1, 1, 2, 1])
#     return a if arr.count(a) == 1 else b


# find_uniq2()
# number = {"1": 2, "2": 1}
# print("1" in number)
# number["3"] = 1
# print(number)


def find_it(seq):
    count_num_dict = dict()
    for num in seq:
        if num in count_num_dict:
            count_num_dict[num] += 1
        else:
            count_num_dict[num] = 1
    print(count_num_dict)
    for num in count_num_dict:
        if count_num_dict[num] % 2 != 0:
            return num
    return


print(find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))


def find_it2(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


print(find_it2([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))