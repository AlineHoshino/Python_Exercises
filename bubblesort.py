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
