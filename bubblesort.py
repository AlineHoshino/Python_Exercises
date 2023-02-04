def bubble(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


print(
    bubble(
        [
            6,
            7,
            8,
            3,
            10,
            19,
            4,
            1,
            0,
            61,
            30,
            16,
            17,
            82,
            29,
            34,
            43,
            21,
            11,
            39,
            56,
            67,
            12,
        ]
    )
)


def turn_into_dictionary(word):
    i_case = word.lower()
    new_word = dict()
    for i in range(len(i_case)):
        count = 0
        for j in range(len(i_case)):
            if i_case[i] == i_case[j]:
                count += 1
            new_word[f'{i_case[i]}'] = count
    return new_word


def duplicate_encode(word):
    dict_word = turn_into_dictionary(word)
    list_word = list()
    i_case = word.lower()
    for letter in i_case:
        if dict_word[letter] == 1:
            list_word.append("(")
        else:
            list_word.append(")")
    return ''.join(str(e) for e in list_word)


print(duplicate_encode("Success"))


def likes(names):
    if len(names) == 0:
        return "no one likes this"
    if len(names) == 1:
        return f"{names[0]} likes this"
    if len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    if len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        qtde = len(names) - 2
        return f"{names[0]}, {names[1]} and {qtde} others like this"


def unique_in_order(sequence):
    str_list = list(sequence)
    print(str_list)
    array = list()
    if len(str_list) == 0:
        return []
    if len(str_list) == 1:
        return str_list
    for i in range(len(str_list) - 1):
        if str_list[i] != str_list[i + 1]:
            array.append(str_list[i])
    array.append(str_list[-1])
    return array


def unique_in_order2(iterable):
    """
    Peguei o exemplo dessa resolução no codewars, a primeira letra
    já entra no array
    e as próximas letras são comparadas com a ultima letra que entrou no array
    se fro diferente entra no array
    """

    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res


print(unique_in_order('A'))
