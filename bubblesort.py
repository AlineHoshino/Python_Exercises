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


def duplicate_encode(word):
    new_word = dict()
    for i in range(len(word)):
        count = 0   
        for j in range(len(word)):
            if word[i] == word[j]:
                count+=1 
            new_word[f'{word[i]}'] = count   
    return new_word


print(duplicate_encode("din"))