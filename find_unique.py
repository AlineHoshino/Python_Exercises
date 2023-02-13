def find_uniq(arr):
    count_number = dict()
    for item in arr:
        if item in count_number:
            count_number[item] += 1
        else:
            count_number[item] = 1
    for item in count_number:
        if count_number[item] == 1:
            return item
    return


print(find_uniq([1, 1, 1, 2, 1]))


def find_uniq2(arr):
    a, b = set([1, 1, 1, 2, 1])
    return a if arr.count(a) == 1 else b


find_uniq2()
number = {"1": 2, "2": 1}
print("1" in number)
number["3"] = 1
print(number)
